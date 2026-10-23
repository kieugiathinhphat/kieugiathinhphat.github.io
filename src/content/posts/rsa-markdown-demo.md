---
title: "Thử viết một bài kỹ thuật: RSA"
description: "Ví dụ bài viết với Markdown, code Python, hình ảnh và công thức LaTeX."
pubDate: 2026-10-24
type: Notes
---

Đây là **bài viết mẫu** để kiểm tra những gì website hỗ trợ. Bạn có thể sửa hoặc xóa bài này bất cứ lúc nào. Nội dung bên dưới chỉ minh họa cách xen kẽ văn bản, code, công thức và hình ảnh.

## 1. Văn bản và Markdown

Bạn có thể viết *in nghiêng*, **in đậm**, thêm [liên kết GitHub](https://github.com/), dùng `inline code`, trích dẫn và bảng.

| Ký hiệu | Ý nghĩa |
| --- | --- |
| $p, q$ | Hai số nguyên tố |
| $n$ | Tích của $p$ và $q$ |
| $e, d$ | Số mũ công khai và bí mật |

> Một bài viết kỹ thuật vẫn nên dễ đọc, ngay cả khi có nhiều công thức.

## 2. Công thức LaTeX

Với hai số nguyên tố $p$ và $q$, đặt $n=pq$. Quá trình mã hóa:

$$
c \equiv m^e \pmod{n}
$$

Quá trình giải mã:

$$
m \equiv c^d \pmod{n}
$$

Các công thức ngắn như $\varphi(n)=(p-1)(q-1)$ cũng có thể nằm **ngay trong đoạn văn**.

## 3. Code có tô màu cú pháp

Để thử RSA bằng Python trên các số nhỏ:

```python
p, q = 61, 53
n = p * q
e, d = 17, 2753

message = 42
cipher = pow(message, e, n)
plain = pow(cipher, d, n)

print(f"ciphertext = {cipher}")
print(f"decrypted = {plain}")
```

Kết quả giải mã là **42**, đúng với thông điệp ban đầu. Đây chỉ là ví dụ học thuật, không phải triển khai RSA an toàn cho thực tế.

Code block cũng có thể dùng cho C++, Bash, JavaScript, JSON, v.v.

```bash
python rsa_demo.py
```

## 4. Chèn hình minh họa

![Sơ đồ mã hóa RSA minh họa](/images/rsa-flow.svg)

Để thêm ảnh khác, đặt file vào `public/images/`, rồi chèn:

```md
![Mô tả ảnh](/images/ten-anh.png)
```

## 5. Các dạng nội dung khác

- [x] Markdown với tiếng Việt có dấu
- [x] Code highlighting
- [x] Ảnh minh họa
- [x] LaTeX inline và display
- [x] Bảng và trích dẫn

Tất cả nằm trong **một file `.md`**, không cần HTML riêng cho từng bài.
