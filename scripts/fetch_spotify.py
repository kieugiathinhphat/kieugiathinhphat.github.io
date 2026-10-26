#!/usr/bin/env python3
"""Build-only Spotify snapshot. Never store or print OAuth credentials."""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUTPUT = Path(__file__).resolve().parents[1] / "src" / "data" / "spotify.json"


def fetch_json(request):
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        try:
            details = json.loads(error.read().decode("utf-8"))
            code = details.get("error", "HTTP error")
            if isinstance(code, dict):
                code = code.get("status", error.code)
        except (ValueError, UnicodeDecodeError):
            code = "HTTP error"
        if code == "invalid_grant":
            raise RuntimeError("Refresh token expired or revoked. Reauthorize Spotify and update the GitHub secret.") from None
        raise RuntimeError(f"Spotify returned HTTP {error.code} ({code}).") from None


def main():
    client_id = os.environ.get("SPOTIFY_CLIENT_ID", "").strip()
    refresh_token = os.environ.get("SPOTIFY_REFRESH_TOKEN", "").strip()
    if not client_id or not refresh_token:
        raise RuntimeError("Missing SPOTIFY_CLIENT_ID or SPOTIFY_REFRESH_TOKEN GitHub Actions secret.")

    body = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
    }).encode("utf-8")
    token = fetch_json(urllib.request.Request(
        "https://accounts.spotify.com/api/token",
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    ))

    if token.get("refresh_token") and token["refresh_token"] != refresh_token:
        print("::warning::Spotify issued a new refresh token. Reauthorize locally if future updates fail; never print tokens.")

    access_token = token.get("access_token")
    if not access_token:
        raise RuntimeError("Spotify did not return an access token.")

    top = fetch_json(urllib.request.Request(
        "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=5",
        headers={"Authorization": f"Bearer {access_token}"},
    ))
    tracks = []
    for item in top.get("items", []):
        url = (item.get("external_urls") or {}).get("spotify", "")
        images = (item.get("album") or {}).get("images") or []
        image = images[1]["url"] if len(images) > 1 else (images[0]["url"] if images else "")
        if not url.startswith("https://open.spotify.com/track/"):
            continue
        if image and not image.startswith("https://i.scdn.co/"):
            image = ""
        artists = ", ".join(a.get("name", "") for a in item.get("artists", []) if a.get("name"))
        tracks.append({
            "title": item.get("name", ""),
            "artist": artists,
            "url": url,
            "image": image,
        })

    if not tracks:
        raise RuntimeError("Spotify returned no top tracks. Keeping the previous published site.")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "period": "Last 4 weeks",
        "tracks": tracks,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Spotify snapshot ready: {len(tracks)} tracks (no credentials stored).")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, urllib.error.URLError, TimeoutError, ValueError) as error:
        print(f"::warning::{error}", file=sys.stderr)
        sys.exit(1)
