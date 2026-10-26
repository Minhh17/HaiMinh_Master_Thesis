# Agent instructions

Đọc theo thứ tự: [context](ai/project-context.md), [current state](ai/current-state.md),
[next actions](ai/next-actions.md), [planning index](planning/README.md), tracker Excel
và báo cáo tuần Word đang làm, rồi design/ADR liên quan. Không dựa vào lịch sử chat.

## Quy ước người dùng xác nhận ngày 2026-10-24

- Học viên tự cài và quản lý môi trường. Không tự chạy `make help`, `make doctor`,
  `make vivado-check`, `make check`, test/build hoặc cài công cụ. Chỉ thực thi khi người dùng
  yêu cầu rõ ở phiên sau; không yêu cầu chạy lệnh để hoàn tất một việc tài liệu.
- Giữ cấu trúc đã thu gọn: engineering/source nằm trong `Project_source/`.
  Tận dụng thư mục hiện có, không tự tách thêm nhiều folder.
- Ưu tiên Word/Google Docs cho đề cương, báo cáo, tài liệu học thuật; Excel/Google Sheets
  cho kế hoạch và tiến độ. Dùng `.md` cho README, AI instructions/context và tài liệu kỹ thuật
  cần đi cùng code; không tạo nhiều bản Markdown của cùng một plan/report.
- Kế hoạch/trạng thái công việc đang dùng nằm trong `planning/Project_Tracker_HK1_Nguyen_Hai_Minh.xlsx`.
  Báo cáo GVHD là bản chụp theo tuần: tiến độ tuần này; khó khăn và cách giải quyết; ý nghĩa thiết kế;
  nhiệm vụ tuần tới. Chu kỳ thứ Hai–Chủ nhật, tuần 01 bắt đầu 26/10/2026. Không tự gửi báo cáo cho thầy hoặc đánh dấu đã gửi.

- Phạm vi hiện tại: Phase 1 Ibex SoC, C firmware, UART/GPIO/timer/interrupt/debug và baseline.
  Board TBD; Ibex là preferred candidate. Không tự triển khai accelerator/custom DSP/RF.
- Vivado CONFIRMED BY USER; khả năng chạy của agent, license, build, timing và physical
  bring-up là các trạng thái độc lập. Không ghi PASS nếu chưa có lệnh/log/bằng chứng.
- Dùng PASS / FAIL / BLOCKED / NOT RUN cho test; phân biệt source inspection, inference,
  simulation và hardware measurements. AI draft không phải kiến thức người học đã xác nhận.
- `knowledge/`: lời giải thích cá nhân; `research/`: nguồn/giả thuyết; `docs/`: thiết kế;
  `experiments/`: run và bằng chứng. Không sao chép một nội dung thành nhiều nguồn trạng thái.
- Không thêm DOI, số liệu, novelty hoặc citation chưa kiểm tra. Ghi nguồn, revision/ngày đọc,
  phạm vi đã đọc và điều nguồn không chứng minh. Raw dataset/PDF cần quyền và license rõ ràng.
- Giữ nguyên input và công việc đang có. Không xóa/reset checkout để “sửa” lỗi môi trường.
  Không commit build artifacts, secrets, license, dữ liệu thô hay upstream source.
- Dùng pin và flow upstream; `third_party/checkouts/` bị ignore. Không tự cập nhật dependency.
- Yêu cầu người dùng phê duyệt trước destructive operations, external publishing/push,
  data/nontrivial source downloads, proprietary installs hoặc mua board, trừ khi phiên hiện tại
  đã cấp quyền rõ ràng. Đọc public docs không cần phê duyệt. Không tự gửi tin nhắn cho người khác.
- Kiểm tra tài liệu bằng cách đọc lại file tạo/sửa. Không chạy toolchain/test theo mặc định.
- Sau task: cập nhật tracker khi có thay đổi tiến độ thật, evidence/test matrix nếu có,
  `ai/current-state.md`, tối đa năm next actions và handoff theo template.
- Thay đổi nhỏ, review được; không tự chọn identity Git hoặc license. Trước remote push
  kiểm tra staged files, ignore rules và xin phê duyệt cụ thể.

Quy trình: [development](ai/workflows/development.md), [research](ai/workflows/research.md),
[experiment](ai/workflows/experiment.md), [documentation](ai/workflows/documentation.md).

- Khi dạy: soạn giải thích kiến thức, ví dụ giải, bài tự làm và thực hành gắn khối RISC-V;
  bám sách Hennessy/Patterson 6th edition với mục/trang đã đọc và đối chiếu ISA. Không chỉ
  đưa reading guide. Đầu ra học thuật Word; chưa xác nhận người học hiểu/đạt khi chỉ có AI draft.
