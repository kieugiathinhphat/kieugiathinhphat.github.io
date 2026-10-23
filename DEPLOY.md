# Hướng dẫn đưa website lên GitHub Pages

Repository: `kieugiathinhphat/kieugiathinhphat.github.io`  
Website: `https://kieugiathinhphat.github.io`

1. Tạo repository Public tại https://github.com/new (để trống, không tích Create README).
2. Mở terminal trong thư mục có `package.json` và chạy:

```bash
git init
git add .
git commit -m "Initial personal website"
git branch -M main
git remote add origin https://github.com/kieugiathinhphat/kieugiathinhphat.github.io.git
git push -u origin main
```

3. Vào repository → Settings → Pages → Source → GitHub Actions.
4. Nếu cần, vào tab Actions → Deploy Astro to GitHub Pages → Run workflow.
5. Khi workflow xanh, truy cập https://kieugiathinhphat.github.io.

Để cập nhật nội dung: sửa `.md` trong `src/content/posts/`, sau đó:

```bash
git add .
git commit -m "Update posts"
git push
```

**Lưu ý:** Thay `username`, avatar, email placeholder và bài mẫu trước khi chia sẻ công khai.
