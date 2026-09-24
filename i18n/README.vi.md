[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*Thư viện mở có thể tải xuống dành cho Bunko.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

Kho này lưu 150 ấn bản hoàn chỉnh của tác phẩm kinh điển thuộc phạm vi công cộng dưới dạng các chương JSON gọn nhẹ, kèm cách đọc ruby và bìa minh họa đã kiểm tra không có chữ. Bunko chỉ tải các chương được mở rồi lưu để đọc ngoại tuyến. Ứng dụng ở kho [Bunko](https://github.com/lachlanchen/Bunko); thêm sách đã duyệt ở đây không cần tạo lại ứng dụng.

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="Bìa minh họa không chữ" width="300"></a></p>

## Trong thư viện

| Đường dẫn | Mô tả |
| --- | --- |
| [`books/`](../books/) | Thư mục sách: siêu dữ liệu, quyền và tệp chương |
| [`reader-index.json`](../reader-index.json) | Danh mục được tạo cho trình đọc |
| [`tools/`](../tools/) | Bộ kiểm tra, công cụ tạo danh mục và bài thử |

## Xuất bản và kiểm tra

Dùng [trang quản lý thư viện](https://lachlan.lazying.art/Bunko/admin/) để chuẩn bị pull request cho sách, hoặc sửa `books/<id>/` bằng Git. Hãy đọc [hướng dẫn xuất bản](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md) trước. Quy trình kiểm tra mọi chương và hồ sơ quyền, rồi tạo lại `reader-index.json` sau khi gộp; đừng sửa chỉ mục này bằng tay.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## Quyền và tương thích

Mỗi gói cần `meta.json`, `rights.json` và các chương gọn; bìa đã kiểm tra không có chữ là tùy chọn. [Bản kiểm tra ấn bản](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) ghi căn cứ tác phẩm gốc. Chủ sở hữu xác nhận bản dịch cuối do Codex tạo. Giữ các chương cũ có tên theo nội dung cho người đọc đã lưu bộ nhớ đệm. Tình trạng phạm vi công cộng có thể khác theo lãnh thổ.


## Ủng hộ thư viện

Bunko Books là thư viện công cộng của LazyingArt. Sự hỗ trợ giúp duy trì danh mục và công cụ đọc:

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Trích dẫn

Nếu dùng Bunko Books trong nghiên cứu, hãy trích dẫn kho này. GitHub đọc [CITATION.cff](../CITATION.cff) và hiển thị bảng trích dẫn.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## Đính chính

Để báo thiếu nội dung, lỗi siêu dữ liệu, bìa hoặc vấn đề quyền, hãy [mở issue cho sách](https://github.com/lachlanchen/bunko-books/issues/new). Bản kiểm tra là hồ sơ minh bạch, không phải chứng nhận pháp lý toàn cầu.
