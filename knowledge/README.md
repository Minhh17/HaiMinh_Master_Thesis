# Kế hoạch học CA01–CA08

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

## Điểm bắt đầu

- [RV32I và pipeline Ibex](ibex-microarchitecture/rv32i-fetch-decode-execute.md): tách hành vi ISA khỏi tổ chức pipeline, có bài tập tay.
- [MMIO và memory map](soc-and-buses/mmio-memory-map.md): cách truy nguồn một địa chỉ; không bịa địa chỉ SoC.
- [Nhật ký học](learning-journal/README.md): mỗi phiên ghi một điều hiểu, một evidence và một câu hỏi.

## Đọc Patterson & Hennessy có mục tiêu

Tham chiếu *Computer Organization and Design RISC-V Edition*, 2nd edition, David A. Patterson và John L. Hennessy; mục lục được đối chiếu tại [nhà xuất bản Elsevier](https://shop.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6) ngày 2026-10-23. Không lưu bản PDF chưa có quyền sử dụng vào repo.

| Phần nên đọc | Dùng cho bài tập |
| --- | --- |
| Chương 1 — abstraction và performance | Phân biệt ISA, microarchitecture, SoC; định nghĩa metric |
| Chương 2 — instruction set | Giải mã lệnh và đọc disassembly (CA01–CA02) |
| Chương 3 — arithmetic | Width, signedness, overflow; chuẩn bị kiến thức DSP sau Phase 1 |
| Chương 4 — processor | Datapath/pipeline rồi đối chiếu Ibex; không áp nguyên pipeline sách lên core |
| Chương 5 — memory hierarchy | Hiểu latency và data movement; không giả định baseline có cache |
| Phụ lục A — logic design | Ôn combinational/sequential logic trước khi đọc RTL |

Đây là gợi ý đọc theo chủ đề, không chép nội dung/bài giải sách. Với bản khác, đối chiếu tên chương thay vì suy trang/số mục. Đọc ISA từ [RISC-V Ratified Specifications](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html), cấu hình core từ [Ibex docs](https://ibex-core.readthedocs.io/en/latest/), wiring/build từ [Demo System](https://github.com/lowRISC/ibex-demo-system); pin thực tế có thể khác tài liệu `latest`.

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
