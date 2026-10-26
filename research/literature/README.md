# Literature workflow

## Sách chính và bản PDF cục bộ

Theo lựa chọn của người dùng ngày 2026-10-24, sách chính cho việc học kiến trúc máy tính
từ đây là **Computer Architecture: A Quantitative Approach, Sixth Edition**,
John L. Hennessy và David A. Patterson.

- [Mở sách PDF](<../../Tài liệu/Computer_Architecture_A_Quantitative_Approach_6th_Edition.pdf>).
- Thư mục [Tài liệu](<../../Tài liệu/>) chứa sách và PDF bài báo người dùng bổ sung;
  chỉ mục, bibliography và ghi chú nguồn tiếp tục nằm trong `research/literature/`.
- Nguồn: file người dùng cung cấp, chuyển từ root và rút gọn tên file; không tải thêm.
  Đã đối chiếu tên, tác giả, ấn bản và mục lục từ phần đầu PDF ngày 2026-10-24
  (`METADATA-ONLY` ở phiên 24/10). Ngày 26/10 đã đọc chọn lọc §1.3, §1.9 tr.52–53,
  A.9 (A-33–A-40), C.1 (C-2–C-6) để soạn bài học; không phải full-text review
  và chưa xác nhận người học đã nắm. Bài học ghi rõ số trang sách/PDF, phạm vi RV64G/RV32I.
- SHA-256 sau chuyển, trùng bản đầu vào:
  `e8a85afe55c3874802c3b9f98f97028b17e8da415067a0252c4800d61a5d6400`.
- PDF được giữ cục bộ, đã có quy tắc `*.pdf` trong `.gitignore`. Bản sách có thông báo
  bản quyền; quyền phân phối lại chưa xác minh. Không đưa PDF vào Git/publish.

Khi hướng dẫn học, dùng đúng cuốn và ấn bản này; đối chiếu chương/mục trong PDF trước
khi giao phần đọc. Sách cung cấp nền tảng lý thuyết, không xác nhận cấu hình hoặc kết quả
đo Ibex/FPGA của dự án. Xem [knowledge index](../../knowledge/README.md).

## Quản lý bài báo

[literature-matrix.csv](literature-matrix.csv) là chỉ mục bài; [references.bib](references.bib) là bibliography chuẩn duy nhất. Hiện matrix chỉ có header và bibliography để trống: chưa kiểm chứng trọn bộ metadata của một bài để đưa vào danh mục. Các URL dataset trong [catalog](../../datasets/catalog.md) là nguồn kiểm tra ứng viên, không đồng nghĩa đã review bài liên quan.

1. Dùng publisher, DOI landing page hoặc bản tác giả để xác minh title, authors, year, venue và DOI. Phân biệt preprint với bản xuất bản; ghi version và ngày truy cập.
2. Sao chép [paper template](papers/paper-template.md) thành `papers/PAPER-001-short-title.md`. Ghi `ABSTRACT-ONLY`, `FULL-TEXT-REVIEWED` hoặc `METADATA-ONLY`; AI draft chưa được người học xác nhận phải ghi rõ.
3. Điền matrix, dùng cùng `paper_id` cho note và citation key. Dùng ô trống cho trường chưa biết; không thay thiếu dữ liệu bằng số 0. CSV chứa dấu phẩy phải quote theo chuẩn CSV.
4. Số liệu phải có đơn vị, điều kiện đo, baseline và vị trí table/figure/page. Phân biệt số tác giả báo cáo với số tự tính và phép suy luận.
5. Chỉ thêm BibTeX sau khi đối chiếu danh tính. Không chép abstract hoặc nội dung bài dài vào repository; giữ ghi chú tự viết và liên kết hợp lệ.

Các cột `evidence_status`, `review_scope` và `learner_verified` độc lập: kiểm chứng metadata không đồng nghĩa thẩm định thí nghiệm. `notes_path` tính từ root repository; `source_url` là nguồn gốc, không phải trang kết quả tìm kiếm.

## Bài học đang dùng — 26/10/2026

[Bài học RV32I bằng Word](../../knowledge/computer-architecture/Bai_hoc_RV32I_Tuan_01_2026-10-26.docx)
đưa ra giải thích, ví dụ tự xây dựng, bài thực hành và kết quả kỳ vọng. Sách là trục lý thuyết;
[RV32I v2.1 tại thư viện v20260120](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)
là nguồn đối chiếu encoding/ngữ nghĩa, đã mở ngày 26/10. XML T3 và đề BTL đã đọc từ
`/home/haiminh/Documents/MasterHust/KienTrucMayTinhTienTien/`; các nhận xét mạch chỉ là
source inspection, không phải simulation. Chưa sửa bản mạch nguồn.
