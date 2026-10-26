# Workspace handoff — 2026-10-23

Các phần khởi tạo dưới đây là lịch sử ngày 23/10. Bàn giao mới nhất ở
[phiên đồng bộ Git 24/10](#git-sync-2026-10-24); quy ước hiện hành xem [AGENTS](AGENTS.md).

**Đã tạo khung workspace có thể dùng ngay**, theo [spec v1.1](IBEX_THESIS_WORKSPACE_SPEC_v1.1.md)
và xác nhận tiếp theo: chỉ cần khung; Vivado nằm trên server, cấu hình để TBD.
Vị trí: `/home/haiminh/Desktop/Master_Thesis/riscv-ibex-thesis`.
Git local, branch `workspace/bootstrap`; không remote/push. Đặc tả gốc được giữ nguyên.

## Nội dung đã tạo

```text
riscv-ibex-thesis/
├── README.md, AGENTS.md, Makefile, Git/editor configuration
├── .github/                 CI, task/bug/experiment/reading issues, PR template
├── planning/                WP1–6, CA01–08, W1–W8, backlog, milestones, Week 1
├── knowledge/               index, 2 sourced draft notes, learning templates
├── research/                paper workflow, matrix, provisional RQ/H/gaps
├── docs/                    architecture, design, ADRs, guides, tests, reports
├── hardware/ firmware/      entry points for own RTL and C
├── simulation/ fpga/        upstream runbooks, board TBD, report Tcl
├── dsp/                     future scope only
├── datasets/                provenance/license manifest, candidate catalog
├── experiments/             run configuration and result templates
├── thesis/                  outline, claim-to-evidence index
├── third_party/             source pins, acquisition instructions
├── scripts/                 doctor, validator, checkout/build guards, tests
├── tools/                   detected versions, check dependencies
└── ai/                      context/state/next actions/workflows/handoff
```

Nhóm chưa hoạt động dùng README có scope; thêm thư mục con khi có source thật.
Xem [ADR-0001](docs/decisions/ADR-0001-workspace-architecture.md). Không có RTL/firmware giả,
dataset download hoặc copied vendor source. Bibliography trống có chủ ý, không tạo citation giả.

## Kiểm chứng thực tế

| Lệnh/phạm vi | Kết quả |
|---|---|
| `make help` | PASS, exit 0 |
| `make doctor` | PASS inventory, exit 0; thiếu tool ghi BLOCKED riêng |
| `make check` | PASS: file/link/config checks, 34 ignore/track cases, 13 utility tests |
| Isolated RV32IMC object compile/readelf | PASS; không phải upstream firmware link/run |
| `make vivado-check` | BLOCKED, exit 2; Vivado server USER-AVAILABLE |
| `python3 scripts/setup/upstream.py` | BLOCKED, exit 2; checkout chưa tải |
| `make sim` | BLOCKED, exit 2; thiếu checkout/FuseSoC/compiler prefix |
| `make fpga` | BLOCKED, exit 2; board TBD và local prerequisites chưa đủ |
| GitHub Actions hosted execution | NOT RUN; chỉ chuẩn bị YAML |
| Vivado Tcl/timing/bitstream/physical board | NOT RUN |

Output thực: [validation report](docs/reports/workspace-validation-2026-10-23.md).
Versions/giới hạn: [tool inventory](tools/tool-versions.md). Đây là kiểm chứng khung workspace,
không xác nhận build compatibility, RTL correctness hoặc hardware. Link check chỉ xét local
file paths, không render Mermaid hoặc validate mọi anchor/URL. Hygiene scan là kiểm tra nhẹ.

## Phần để dành

Vivado **CONFIRMED BY USER — trên server**; version/edition/license/path/access TBD theo yêu cầu.
Board TBD; chưa tự chọn device/XDC. Source pins đã đối chiếu nguồn chính thức, chưa checkout/build;
Python transitive dependencies chưa khóa đầy đủ. License phần tự viết chưa chọn.
Cài toolchain, tải source/dataset, chạy build/board và GitHub thuộc công việc sau.
Không cần cung cấp server hoặc chọn board để bắt đầu dùng khung.

## Sử dụng và bước kế tiếp

```sh
cd /home/haiminh/Desktop/Master_Thesis/riscv-ibex-thesis
make help
make doctor
make check
```

Mở [README](README.md), [roadmap](planning/roadmap.md), [Week 1](planning/weekly/week-01.md),
[AGENTS](AGENTS.md), [current state](ai/current-state.md), [simulation lab](docs/guides/simulation.md),
[Vivado server runbook](docs/guides/vivado-workflow.md).

Năm việc khi bắt đầu triển khai; prerequisites/DoD tại [next actions](ai/next-actions.md):

1. Ghi cấu hình Vivado server khi cần build, hiện để TBD.
2. So sánh board, ghi ADR khi người dùng chọn.
3. Lấy pinned checkout và cài môi trường khi được yêu cầu tải/cài.
4. Build simulator, sau đó kiểm tra firmware execution riêng.
5. Học CA01–CA02 và sửa starter notes bằng lời giải thích của mình.

Phiên này tạo các file scaffold trong repo mới, kiểm tra bằng những lệnh ghi ở report.
Open questions: server/tool/board/license. Xem revision bằng `git log -1 --oneline`
và working tree bằng `git status --short`. Không tạo tag hardware baseline.

## Session handoff 2026-10-24

- **Thời gian / task / tác giả:** 24/10/2026, 22:18 (Asia/Phnom_Penh);
  sắp xếp sách và ghi nhận học liệu chính, không tạo mã task học mới; Codex.
- **Revision / trạng thái:** `main`, `d15e1e6`; working tree đã có thay đổi từ trước.
  Các chỉnh sửa có sẵn được giữ lại; không commit/push.
- **Yêu cầu / phạm vi:** chuyển sách Computer Architecture người dùng vừa thêm vào nơi
  lưu tài liệu cùng PDF bài báo; lưu lựa chọn theo sách này trong các phiên học sau.
- **Tệp thay đổi:** chuyển nguyên vẹn PDF từ root vào `Tài liệu/`, rút gọn tên file;
  thêm README của thư mục và liên kết ở README gốc. `research/literature/README.md`
  ghi danh tính, nguồn và checksum; `knowledge/README.md` chuyển sách chính từ gợi ý cũ
  sang *Computer Architecture: A Quantitative Approach*, bản 6.
  Tracker Excel cập nhật danh mục học liệu; AI context/state/next actions ghi lựa chọn.
- **Lệnh thực tế / bằng chứng:** `pdftotext` đọc phần đầu PDF (exit 0);
  `python3` chuyển file, đối chiếu SHA-256 và đọc lại tài liệu/liên kết (exit 0);
  `git check-ignore -v` xác nhận PDF khớp `*.pdf` (exit 0).
  Lượt đọc tracker bằng `python` ban đầu lỗi thiếu `pathlib`, đã đọc lại bằng `python3`.
  Danh tính và checksum lưu tại [literature index](research/literature/README.md).
- **Kiểm chứng:** PASS — PDF trước/sau cùng SHA-256; đọc lại nội dung và liên kết cục bộ
  đã sửa. Tracker chỉ đổi `Chi tiet HK1!H42` và thêm học liệu R8 ở hàng 50, kèm định dạng
  hàng đó; mọi công thức và nội dung khác giữ nguyên, 12 thành phần ZIP khác trùng từng byte.
  Đã đọc lại năm ô thay đổi và xác nhận đường dẫn PDF tồn tại. Bằng chứng kiểm tra tạm:
  `/tmp/computer_archi_tracker_nw4stu9l/verification.json`.
  Đây là kiểm tra tài liệu, không phải kiểm chứng RTL/hardware.
  Test dự án, Make, build, simulation và FPGA: **NOT RUN**.
- **Quyết định:** dùng sách người dùng cung cấp làm nguồn lý thuyết chính;
  PDF lưu ở `Tài liệu/`, ghi chú nguồn tiếp tục ở `research/literature/`.
  Không có thay đổi kiến trúc cần ADR mới.
- **Giới hạn:** mới đối chiếu phần đầu/mục lục, chưa review toàn văn hoặc xác nhận
  người học đã hoàn thành phần đọc; lịch và tiến độ học không tăng vì sắp xếp tài liệu.
- **State / next actions:** cập nhật `ai/project-context.md`, `ai/current-state.md`;
  vẫn giữ tối đa năm mục ở `ai/next-actions.md`.
- **Bước nhỏ tiếp theo:** khi bắt đầu buổi học, đối chiếu chủ đề đang làm trong tracker
  với chương/mục thật của sách; đầu ra là phần đọc và bài tập phù hợp với mức hiểu hiện tại.

## Git sync 2026-10-24

- **Ngày / task / tác giả:** 24/10/2026 (Asia/Phnom_Penh); đồng bộ cập nhật tài liệu; Codex.
- **Yêu cầu và quyền:** người dùng yêu cầu “giờ push lên git đi”; áp dụng cho bộ cập nhật
  tài liệu hiện có, gồm quy ước Word/Excel, mẫu/nháp báo cáo tuần, tracker và học liệu chính.
- **Revision / đích:** bắt đầu tại `main`, `d15e1e6`; `origin/main` cùng revision khi đọc
  bằng `git ls-remote` (exit 0). Remote là `Minhh17/HaiMinh_Master_Thesis`, hiện public;
  kết nối GitHub xác nhận quyền push. Dùng identity Git đã cấu hình.
- **Phạm vi:** commit các tài liệu đã rà soát và push thường lên `origin/main`;
  không force-push. PDF sách tiếp tục ở local theo `.gitignore`.
- **Kiểm tra chuẩn bị:** đọc diff, nội dung hai Word và danh mục học liệu Excel;
  không thấy secrets/build artifacts trong danh sách thay đổi. `git check-ignore -v`
  xác nhận PDF bị bỏ qua (exit 0). Lần truy cập GitHub trong sandbox bị lỗi DNS;
  lần truy cập có quyền mạng thành công. Không chạy Make/test/build (**NOT RUN**).
- **State / hành động tiếp:** README và `ai/current-state.md` phản ánh remote hiện có;
  tracker không đổi tiến độ vì đồng bộ Git. Năm mục `ai/next-actions.md` vẫn áp dụng.
  Trạng thái push cuối cùng phải dựa trên kết quả lệnh và đối chiếu SHA local/remote.


## Phiên tài liệu ngày 26/10/2026 (Asia/Phnom_Penh)

- Task: học theo sách gắn BTL RV32I; tác giả: Codex. Git đầu phiên sạch; chưa commit/push.
- Đầu vào: PDF sách, tracker/báo cáo cũ; đọc thêm T3 và đề BTL tại thư mục môn học.
- Đã chuẩn hóa tên sách, chuyển 9 PDF bài báo vào Tài liệu; checksum trước/sau trùng cả 10.
- Đã soạn bài học Word sáu buổi, giải thích/ví dụ/bài thực hành; bảng expected không phải log.
- Đã cập nhật mẫu/báo cáo tuần Word có ý nghĩa thiết kế; chuyển lịch 26/10–01/11 theo xác nhận
  người dùng; báo cáo 21–27/10 giữ làm lịch sử. Tracker thêm kế hoạch tuần, giữ công thức cũ.
- Đã đọc lại DOCX/XLSX bằng python-docx/openpyxl (exit 0); tính lại các mã S/B trong ví dụ.
  Không có đoạn Kiểm tra workspace/direct utility tests/PyYAML trong báo cáo mới.
- PASS: đọc lại cấu trúc Word/Excel, công thức tracker và kiểm tra bảo toàn PDF bằng SHA-256.
  NOT RUN: Logisim, build/toolchain, FPGA. Không nâng trạng thái học hay verification matrix.
- Preview PDF bằng LibreOffice thất bại trong sandbox (exit 1; dconf/read-only ở lần đầu,
  lần gọi trực tiếp không có chẩn đoán). Chưa kiểm chứng bố cục bằng render; không cài công cụ.
- Nguồn học: §1.3; §1.9 tr.52–53; A.9 A-33–40; C.1 C-2–6; RV32I v2.1/library v20260120.
  Phân biệt ví dụ RV64G của sách và RV32I của BTL; branch target lấy PC lệnh + byte offset.
- Chưa biết: trình độ thực tế, giờ thực tế, kết quả khối, GVHD/ngày gửi. Không suy ra từ tài liệu.
- Next action nhỏ nhất: học viên giải thích Q/D rồi dựng PC+4; lưu bảng trước–sau cạnh.
