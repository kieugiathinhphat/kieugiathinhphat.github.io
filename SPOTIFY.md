# Spotify: On repeat

The homepage displays five top tracks from the last ~4 weeks, using the Spotify Web API.
It is a static Astro widget, not a live player or a count of actual plays.

## Setup

1. Authorize your Spotify account locally with `user-top-read` using Authorization Code with PKCE.
2. In the repository, go to Settings > Secrets and variables > Actions.
3. Add repository secrets:
   - `SPOTIFY_CLIENT_ID`
   - `SPOTIFY_REFRESH_TOKEN`
4. Open Actions > **Deploy Astro to GitHub Pages** and choose **Run workflow**.

Workflow runs on pushes to `main`, manual dispatches, and each day (03:17 UTC).
It refreshes the OAuth access token, fetches your top five tracks, generates
`src/data/spotify.json` for that build, and deploys the static output.
The refresh token and access token are never published.

The committed `src/data/spotify.json` contains an empty placeholder. Local
`npm run dev` therefore hides the music module until you supply a non-empty
snapshot. The live website gets its tracks from GitHub Actions.

If Spotify is unavailable, a warning appears in the build job and the blog
still deploys; the music module remains hidden. No fake tracks are shown.

**Spotify refresh tokens expire after 180 days (six months) from authorization.**
Re-run the local PKCE authorization and update `SPOTIFY_REFRESH_TOKEN`
before/when the token expires. Refreshing daily does not extend its lifetime.
If Spotify returns `invalid_grant`, reauthorize; do not retry the expired token.

See: https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens
