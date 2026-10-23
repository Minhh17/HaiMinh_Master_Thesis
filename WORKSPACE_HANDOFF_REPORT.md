# Workspace handoff — 2026-10-23

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
