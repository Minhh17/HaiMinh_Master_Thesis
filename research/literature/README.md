# Literature workflow

[literature-matrix.csv](literature-matrix.csv) là chỉ mục bài; [references.bib](references.bib) là bibliography chuẩn duy nhất. Hiện matrix chỉ có header và bibliography để trống: chưa kiểm chứng trọn bộ metadata của một bài để đưa vào danh mục. Các URL dataset trong [catalog](../../datasets/catalog.md) là nguồn kiểm tra ứng viên, không đồng nghĩa đã review bài liên quan.

1. Dùng publisher, DOI landing page hoặc bản tác giả để xác minh title, authors, year, venue và DOI. Phân biệt preprint với bản xuất bản; ghi version và ngày truy cập.
2. Sao chép [paper template](papers/paper-template.md) thành `papers/PAPER-001-short-title.md`. Ghi `ABSTRACT-ONLY`, `FULL-TEXT-REVIEWED` hoặc `METADATA-ONLY`; AI draft chưa được người học xác nhận phải ghi rõ.
3. Điền matrix, dùng cùng `paper_id` cho note và citation key. Dùng ô trống cho trường chưa biết; không thay thiếu dữ liệu bằng số 0. CSV chứa dấu phẩy phải quote theo chuẩn CSV.
4. Số liệu phải có đơn vị, điều kiện đo, baseline và vị trí table/figure/page. Phân biệt số tác giả báo cáo với số tự tính và phép suy luận.
5. Chỉ thêm BibTeX sau khi đối chiếu danh tính. Không chép abstract hoặc nội dung bài dài vào repository; giữ ghi chú tự viết và liên kết hợp lệ.

Các cột `evidence_status`, `review_scope` và `learner_verified` độc lập: kiểm chứng metadata không đồng nghĩa thẩm định thí nghiệm. `notes_path` tính từ root repository; `source_url` là nguồn gốc, không phải trang kết quả tìm kiếm.
