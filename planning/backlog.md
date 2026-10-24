# Backlog — nguồn duy nhất cho trạng thái task

> Cập nhật 24/10/2026: đây là bản tham chiếu lúc khởi tạo. Kế hoạch/trạng thái đang dùng nằm trong [tracker Excel](Project_Tracker_HK1_Nguyen_Hai_Minh.xlsx); báo cáo tuần dùng Word theo [planning index](README.md). Học viên tự cài môi trường, agent không tự chạy Make/test/build. Khi có khác biệt, ưu tiên tracker đã được học viên cập nhật.

Cập nhật: **2026-10-23**. Owner mặc định: học viên; agent hỗ trợ tạo/review artifact. Không xem note do agent soạn là bằng chứng học viên đã hiểu. Mỗi task chỉ được DONE khi đáp ứng DoD trong [Phase 1](phase1-plan.md) và có đường dẫn bằng chứng tại đây.

Trạng thái: `PLANNED` chưa bắt đầu; `ACTIVE` đang nghiên cứu/chuẩn bị; `IN_PROGRESS` đang triển khai; `BLOCKED` chưa thể làm bước cần thiết với điều kiện hiện có; `DONE` có evidence đáp ứng DoD; `DEFERRED` ngoài phạm vi hiện tại. Trạng thái test riêng là PASS/FAIL/BLOCKED/NOT RUN, không dùng thay trạng thái task.

| ID | WP / việc | Trạng thái | Phụ thuộc | Bằng chứng hiện có hoặc điều kiện còn thiếu |
| --- | --- | --- | --- | --- |
| P0-01 | Nền tảng workspace và handoff | DONE | — | Khung theo phạm vi người dùng xác nhận; [validation](../docs/reports/workspace-validation-2026-10-23.md), [handoff](../WORKSPACE_HANDOFF_REPORT.md); không bao gồm build Ibex |
| P1-01 | WP1 — nghiên cứu Ibex, Demo System, shortlist board | ACTIVE | — | Có nguồn chính thức trong [note/learning plan](../knowledge/README.md); cần học viên đánh giá yêu cầu, ngân sách, khả năng mua/mượn |
| P1-02 | WP1 — chẩn đoán tool/environment và Vivado | ACTIVE | P0-01 | Local inventory đã chạy; Vivado ở server, version/path để TBD theo yêu cầu user; [tool inventory](../tools/tool-versions.md) |
| P1-03 | WP1 — acquire và xác minh immutable upstream pin | PLANNED | P1-02 | Cần checkout thật, URL/SHA/license khớp lock; ghi SHA thực tế khi hoàn tất |
| P1-04 | WP3 — build simulator upstream, chạy C demo | BLOCKED | P1-02, P1-03 | Chưa có evidence tree/toolchain/build/firmware run; dùng [simulation runbook](../docs/guides/simulation.md) |
| P1-05 | WP2 — giải thích CPU/SoC, ISA và pipeline | PLANNED | P1-01 | [Starter note](../knowledge/ibex-microarchitecture/rv32i-fetch-decode-execute.md) chưa được người học kiểm chứng; cần bài tập CA01–CA02 |
| P1-06 | WP2 — truy memory map từ RTL đến driver | PLANNED | P1-03, P1-05 | Cần địa chỉ/offset và file:line tại SHA được pin; [note MMIO](../knowledge/soc-and-buses/mmio-memory-map.md) là hướng dẫn, chưa là map thực |
| P1-07 | WP3 — waveform và kiểm tra luồng load/store/branch | PLANNED | P1-04, P1-06 | Cần trace thực cùng lệnh chạy, cấu hình và giải thích stall |
| P1-08 | WP1 — ADR chọn board và cấu hình build | BLOCKED | P1-01 | Board TBD; cần người dùng xác nhận board có thể tiếp cận, không tự chọn/mua |
| P1-09 | WP4 — synthesis/implementation/bitstream và timing | BLOCKED | P1-02, P1-07, P1-08 | Cần board/part/constraints hợp lệ, Vivado executable và giấy phép phù hợp |
| P1-10 | WP4 — nạp board, reset/clock, boot firmware | BLOCKED | P1-09 | Cần board vật lý, kết nối và log quan sát; build thành công chưa đáp ứng task |
| P1-11 | WP5 — GPIO in/out, UART tx/rx và CLI nhỏ | BLOCKED | P1-10 | Cần hardware baseline, register map và fixture kiểm thử |
| P1-12 | WP5 — timer/interrupt và kiểm tra trap | BLOCKED | P1-11 | Cần firmware, kích hoạt interrupt có kiểm soát, log hành vi mong đợi |
| P1-13 | WP5 — OpenOCD/GDB halt/step/breakpoint | BLOCKED | P1-10 | Cần transport/probe thực hỗ trợ board và bộ tool phù hợp |
| P1-14 | WP6 — lặp lại bài kiểm tra và cycle counters | PLANNED | P1-11, P1-12, P1-13 | Cần protocol đo, số lần lặp, điều kiện, raw logs và tóm tắt |
| P1-15 | WP6 — resource/timing report và rebuild sạch | PLANNED | P1-09, P1-14 | Cần báo cáo đúng build, không suy ra fmax từ clock yêu cầu |
| P1-16 | WP6 — review và baseline v1 có tag | PLANNED | P1-15 | Cần acceptance matrix đóng, báo cáo limitations, lệnh rebuild và revision |
| P2-01 | Software DSP baseline và dataset đánh giá | DEFERRED | P1-16 | Chưa chọn workload; không triển khai accelerator ở Phase 1 |

Khi cập nhật: giữ ID ổn định, thêm link log/report, ghi blocker cụ thể và bước nhỏ nhất để gỡ. Nếu DoD đổi, ghi lý do trong task note; không sửa ngầm yêu cầu để đánh dấu DONE. Link issue bên ngoài chỉ là bản phản chiếu nếu sau này được tạo, không trở thành tracker cạnh tranh.
