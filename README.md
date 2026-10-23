# Minimal Personal Site — Markdown & GitHub Pages

Bản v2 mở rộng từ starter đã duyệt, **giữ nguyên layout 1 cột, Inter, pastel/dark theme, không có logo username ở header và không có copyright footer**.

## Yêu cầu

Node.js **22.23.4 trở lên** và npm. Nếu máy đã cài dependency của phiên bản trước, sau khi cập nhật mã nguồn hãy chạy `npm install` lại.

## Chạy website

```bash
npm install
npm run dev
```

Mở `http://localhost:4321`.

Kiểm tra bản build:

```bash
npm run build
npm run preview
```

## Thêm một bài mới

Tạo file `src/content/posts/ten-bai-viet.md` với nội dung:

````md
---
title: "Tiêu đề bài viết"
description: "Mô tả ngắn (không bắt buộc)"
pubDate: 2026-10-24
type: Notes
draft: false
---

# Bạn không cần đặt H1 ở đây vì giao diện đã in tiêu đề.

Viết **Markdown** bình thường. Có thể thêm `inline code` và liên kết.

## Code

```python
print("Xin chào!")
```

## Toán học

Công thức trong câu: $a^2+b^2=c^2$.

Công thức riêng một dòng:

$$
E = mc^2
$$

## Ảnh

![Mô tả hình](/images/anh-cua-ban.png)
````

Bài sẽ **tự xuất hiện ở homepage**, sắp theo `pubDate` mới đến cũ, và có đường dẫn `/posts/ten-bai-viet/`.

`type` nhận các giá trị: `Project`, `Code`, `Notes`, `Journal`. Đây chỉ là nhãn nhỏ bên cạnh ngày, không tạo trang danh mục riêng. Nếu không điền, mặc định là `Notes`.

Đặt `draft: true` để không công khai một bài chưa xong (bài draft không được build thành trang).

## Hình ảnh

Cho ảnh của bạn vào `public/images/ten-anh.png`, sau đó chèn vào `.md`:

```md
![Chú thích ảnh](/images/ten-anh.png)
```

Bản v2 dùng `public/images/` để dễ thao tác. Ảnh trong `public` không được Astro tự tối ưu; nên nén ảnh trước khi đăng.

## Công thức toán

- Trong câu: `$x^2+y^2=z^2$`.
- Riêng một dòng: dùng `$$` ở hai dòng riêng bao công thức.
- `remark-math` xử lý cú pháp, `rehype-katex` hiển thị công thức. KaTeX không hỗ trợ toàn bộ lệnh của LaTeX, nhưng đáp ứng tốt phần lớn công thức toán kỹ thuật thông dụng.

## Code

Gõ ba dấu backtick cùng ngôn ngữ (`python`, `cpp`, `bash`, `javascript` ...) để tô màu tự động bằng **Shiki**. Chế độ màu của code đồng bộ với light/dark của trang.

## Cấu trúc cần biết

- `src/content/posts/*.md`: nội dung bài viết.
- `src/content.config.ts`: khai báo trường tiêu đề, ngày, type, draft.
- `src/pages/index.astro`: lấy danh sách bài tự động từ Markdown.
- `src/pages/posts/[id].astro`: trang chi tiết chung cho mọi bài.
- `src/styles/global.css`: giao diện chữ, code, ảnh, bảng, LaTeX.
- `astro.config.mjs`: cấu hình Markdown, math, Shiki.
- `public/images/`: hình minh họa.

**Chưa có GitHub Actions hoặc deploy.** Đây là bước bổ sung Markdown, không thay đổi các bước deploy về sau.


## Deploy GitHub Pages (kieugiathinhphat)

Mục tiêu: **https://kieugiathinhphat.github.io/**. Repository phải có tên chính xác
`kieugiathinhphat.github.io`, nằm dưới tài khoản `kieugiathinhphat`.

1. Vào https://github.com/new. Chọn Owner `kieugiathinhphat`, đặt repository name
   `kieugiathinhphat.github.io`, chọn **Public**, không tạo README/.gitignore/license trong GitHub vì mã nguồn đã có.
2. Mở PowerShell trong thư mục này (nơi có `package.json`) và chạy:

   ```powershell
   git init
   git add .
   git commit -m "Initial personal website with Astro"
   git branch -M main
   git remote add origin https://github.com/kieugiathinhphat/kieugiathinhphat.github.io.git
   git push -u origin main
   ```

   Nếu thư mục đã là Git repository, không cần chạy `git init` lần nữa;
   và chỉ thêm `origin` nếu chưa có remote.
3. Trên GitHub mở repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Mở tab **Actions**, workflow **Deploy Astro to GitHub Pages**. Nếu chưa có run tự động
   hoặc run đầu bị bỏ qua trước khi bật Pages, chọn **Run workflow**.
5. Khi workflow có dấu tick xanh, mở https://kieugiathinhphat.github.io/ .

`astro.config.mjs` đã có `site` và không cần `base` vì đây là user site ở root `/`.
File `.github/workflows/deploy.yml` tự build/deploy khi bạn push lên `main`.
GitHub Action chạy Node 24. Bạn **không** cần tự build thư mục `dist/` hoặc tạo branch `gh-pages`.

**Quan trọng:** Trước khi công khai, hãy sửa tên giới thiệu, avatar, email `hello@example.com`
và các bài mẫu trong `src/content/posts/`. Link GitHub trên homepage đã đổi theo tài khoản
đang kết nối. Sau khi chỉnh bài, chỉ cần `git add .`, `git commit` và `git push` để cập nhật.

**Kiểm tra tại máy (khuyến nghị)**: Dùng Node >=22.23.4, chạy `npm install`,
`npm run build`. Nếu có `package-lock.json` sinh ra từ npm, commit cả file đó để
các lần deploy ổn định hơn.
