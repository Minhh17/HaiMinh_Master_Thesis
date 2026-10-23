# Milestones và cổng chấp nhận

Đây là **định nghĩa gate và ngày mục tiêu**, không phải tracker thứ hai. Đọc trạng thái task tại [backlog](backlog.md); một milestone chỉ đạt khi tất cả task gate đã DONE và evidence được review. Chưa tuyên bố milestone FPGA nào hoàn tất trong phiên tạo workspace.

| Mốc | Ngày mục tiêu gốc | Task gate | Evidence tối thiểu |
| --- | --- | --- | --- |
| M0 — workspace dùng được | 2026-10-27 | P0-01 | README/AGENTS/handoff, `make help`, doctor, check thật, hygiene review |
| M1 — môi trường và upstream có provenance | 2026-10-27 | P1-01/02/03 | Nguồn chính thức, tool inventory, URL + immutable SHA + license |
| M2 — bare-metal C trong simulator | 2026-11-03 | P1-04/05 | Build log, firmware output, configuration, bài giải datapath |
| M3 — hiểu map/trace và board quyết định | 2026-11-10 | P1-06/07/08 | Map có file:line, waveform note, board ADR |
| M4 — boot FPGA thật | 2026-11-17 | P1-09/10 | Các bước Vivado tách riêng, timing/resource reports, boot log |
| M5 — IO và điều khiển thời gian/debug | 2026-12-01 | P1-11/12/13 | GPIO/UART/timer/interrupt và halt/step/breakpoint evidence |
| M6 — characterization có thể lặp | 2026-12-08 | P1-14/15 | Protocol đo, repeat data, constraints, rebuild report |
| M7 — Phase 1 baseline v1 | 2026-12-15 | P1-16 | Verification matrix review, revision/tag, limitations và hướng dẫn rebuild |

Nếu trễ: ghi thay đổi lịch trong weekly review với blocker, tác động downstream và mốc mới được thống nhất. Không xóa ngày gốc. Không chuyển sang accelerator để tránh phần bring-up đang thiếu.
