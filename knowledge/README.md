# Học kiến trúc máy tính gắn với đồ án

`knowledge/` chứa lời giải thích do người học kiểm chứng. `docs/` mô tả triển khai thật; `research/` quản lý bằng chứng học thuật. Hai note khởi đầu dưới đây do AI hỗ trợ, **SOURCED DRAFT — chưa được người học kiểm chứng**. Đã mở nguồn ngày 2026-10-23 không đồng nghĩa đã thử nghiệm RTL hoặc hardware.

| Module | Tuần | Chủ đề | Bài tập/đầu ra để người học xác nhận |
| --- | --- | --- | --- |
| CA01 | W1 | Core vs SoC, RV32I/M/C, fetch/decode/execute | Tự vẽ CPU–memory–peripheral, trace 3 lệnh; nêu phần nào thuộc ISA |
| CA02 | W2 | Register file, datapath, assembler/linker | Đối chiếu C/assembly/ELF map, giải thích reset entry và vùng code/data |
| CA03 | W3 | Pipeline, hazards, memory interfaces | Chú thích một waveform load/branch từ simulation thật, phân biệt latency/throughput |
| CA04 | W4 | FPGA mapping, clock/reset, constraints, timing | Giải thích clock constraint, slack, critical path trên đúng report build |
| CA05 | W5 | MMIO, bus transactions, peripheral registers | Truy một GPIO write từ C tới decoder/register, mô tả side effect |
| CA06 | W6 | Interrupt, trap, CSR, debug | Vẽ chuỗi timer → pending → handler → clear/rearm; giải thích halt/step |
| CA07 | W7 | Cycle counter, CPI, profiling | Thiết kế phép đo có overhead/control; không suy CPI từ tài liệu quảng bá |
| CA08 | W8 | Tổng hợp kiến trúc và reproducibility | Trình bày baseline 10 phút, truy một kết luận về log/source, nêu limitations |

Mỗi module chỉ được người học xác nhận khi có lời giải thích tự viết, bài tập và nguồn. Dùng [note template](templates/learning-note.md); task kỹ thuật vẫn theo [backlog](../planning/backlog.md), không thêm bảng phần trăm học.

## Bài học hiện tại — 26/10–01/11/2026

[Bài học RV32I — Word](computer-architecture/Bai_hoc_RV32I_Tuan_01_2026-10-26.docx) là điểm bắt đầu hiện tại:
trạng thái/clock → fetch/decode → register file/ALU → immediate → datapath/next PC →
ý nghĩa thiết kế và liên hệ Ibex. Có giải thích, bài giải mẫu, bài tự làm và bảng expected;
không chỉ giao danh sách trang cần đọc. Sáu buổi học và một buổi báo cáo, dự kiến 10 giờ.
Lịch hiện hành ở tab **Hoc RV32I tuan** trong tracker; bảng CA01–CA08 phía trên là
khung tham chiếu cũ, không phải lịch tuần đang thực hiện. Các mã Cxx trong tracker là mã học kỳ.

## Tài liệu bổ trợ

- [RV32I và pipeline Ibex](ibex-microarchitecture/rv32i-fetch-decode-execute.md): tách hành vi ISA khỏi tổ chức pipeline, có bài tập tay.
- [MMIO và memory map](soc-and-buses/mmio-memory-map.md): cách truy nguồn một địa chỉ; không bịa địa chỉ SoC.
- [Nhật ký học](learning-journal/README.md): mỗi phiên ghi một điều hiểu, một evidence và một câu hỏi.

## Sách chính theo lựa chọn của người học

Từ 2026-10-24, bám theo **Computer Architecture: A Quantitative Approach, Sixth Edition**
của John L. Hennessy và David A. Patterson, do người dùng cung cấp.
[Mở PDF](<../Tài liệu/Computer_Architecture_A_Quantitative_Approach_6th_Edition.pdf>);
[danh tính, phạm vi kiểm tra và vị trí lưu](../research/literature/README.md).
Lựa chọn này thay gợi ý trước về *Computer Organization and Design RISC-V Edition*,
2nd edition; không dùng bảng chương của cuốn đó cho cuốn hiện tại.

Các buổi giải thích và phần đọc tiếp theo lấy sách này làm trục chính, đối chiếu đúng
chương/mục trong bản PDF. CS61C và các học liệu nền tảng trong tracker dùng để bổ trợ khi
cần. Lịch, giờ và trạng thái học vẫn theo tracker Excel; chưa xác nhận đã đọc chương nào.

Ví dụ và khái niệm trong sách cần được đối chiếu với triển khai thực:
ngữ nghĩa ISA tra đặc tả RISC-V, cấu hình core tra tài liệu Ibex, wiring/build tra
Demo System theo revision của dự án. Không suy pipeline, cache hoặc số đo FPGA từ sách.

## Phân vùng ghi chép

| Thư mục | Chỉ thêm khi có nội dung |
| --- | --- |
| `computer-architecture/` | Mô hình execution, latency, throughput, evidence bài tập |
| `riscv-isa/` | Instruction/CSR/ABI cần cho chương trình đang đọc |
| `ibex-microarchitecture/` | Mapping tài liệu → RTL đúng cấu hình |
| `fpga-design/` | Clock/reset/constraints và cách đọc báo cáo |
| `soc-and-buses/` | Address decode, handshake, register semantics |
| `embedded-software/` | Startup, linker, firmware và debug |
| `dsp/` | Từ vựng/tài liệu tương lai; chưa triển khai accelerator |

Các thư mục chưa có note có README phạm vi; không coi việc tạo thư mục là hoàn tất học tập.
