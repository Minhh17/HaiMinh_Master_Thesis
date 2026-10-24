# Current state — 2026-10-24 (Asia/Phnom_Penh)

Đang chuẩn bị Phase 1; chưa có baseline Ibex trên FPGA được xác nhận.
Học viên đã thu gọn engineering/source vào `Project_source/`; giữ cấu trúc hiện tại.
Vivado nằm trên server của học viên, version/path/board còn TBD.

Quy ước mới: học viên tự cài môi trường. Agent không tự chạy `make help`, `make doctor`,
`make vivado-check`, `make check`, test/build hoặc cài công cụ. Phiên 24/10 chỉ chỉnh tài liệu
và báo cáo; không thực thi các lệnh đó. Kết quả kiểm tra ngày 23/10 là lịch sử của cấu trúc cũ,
không được coi là kiểm chứng lại sau khi di chuyển source.

Kế hoạch và trạng thái đang dùng: `planning/Project_Tracker_HK1_Nguyen_Hai_Minh.xlsx`.
Trong lần bổ sung báo cáo trước đó, hai tab kế hoạch được giữ nội dung/công thức;
thêm tab **Bao cao tuan** để ghi tiến độ,
khó khăn, cách giải quyết, nhiệm vụ tuần tới, ngày gửi và góp ý của thầy.

Đã tạo mẫu báo cáo Word và nháp tuần 01 (21–27/10), cập nhật đến 24/10.
Nháp chỉ ghi điều đã xác nhận: có workspace/đề cương/tracker, source đã được gom;
không tuyên bố học viên đã hoàn thành nội dung học, simulation hoặc hardware.
Chưa gửi báo cáo cho thầy. Ưu tiên Word/Docs cho báo cáo và Excel/Sheets cho plan/progress;
Markdown dùng cho index, context và tài liệu kỹ thuật cần đi cùng code.

Kết quả đọc lại ở lần bổ sung báo cáo: 2 Word đều có ba phần; tracker mở lại được và giữ nguyên
cell values/formulas, number formats, merged ranges của hai tab gốc. Không chạy bộ test dự án.
Tiếp tục ở [planning index](../planning/README.md) và [next actions](next-actions.md).

Đã sắp xếp sách người dùng thêm ngày 24/10 vào
`Tài liệu/Computer_Architecture_A_Quantitative_Approach_6th_Edition.pdf`;
checksum trước/sau trùng nhau. Thư mục này dùng chung cho sách và PDF bài báo cục bộ.
Người dùng chọn cuốn này làm sách chính từ đây; knowledge index và danh mục học liệu
trong tracker đã đồng bộ lựa chọn. Chỉ kiểm tra phần đầu/mục lục để nhận diện sách,
chưa xác nhận đã đọc chương nào; không tăng trạng thái hoàn thành công việc học.
PDF vẫn được Git ignore. Handoff phiên này ở `WORKSPACE_HANDOFF_REPORT.md`.

Đồng bộ Git ngày 24/10: người dùng đã yêu cầu commit/push các cập nhật tài liệu.
Remote `origin` là `https://github.com/Minhh17/HaiMinh_Master_Thesis.git`, nhánh `main`;
repository hiện public. Đã xác nhận quyền push, nhánh remote cùng revision gốc `d15e1e6`
và PDF không thuộc danh sách commit. Không thay đổi tiến độ học hoặc trạng thái báo cáo GVHD.
