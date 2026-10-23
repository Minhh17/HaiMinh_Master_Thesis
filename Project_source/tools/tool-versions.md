# Tool inventory — 2026-10-23

Phạm vi: shell local agent, Linux; kết quả probe version, không phải kiểm chứng cả toolchain.
**Vivado: CONFIRMED BY USER, nằm trên server (xác nhận 2026-10-23).** Agent chưa truy cập
server; exact version/edition/license/device support và executable path: UNKNOWN.
`USER-AVAILABLE / AGENT-NOT-VERIFIED` không có nghĩa là Vivado thiếu trên server.

| Tool | Local detection / version | Test thực hiện / giới hạn |
|---|---|---|
| Git | 2.25.1 | version PASS; local repo init và ignore checks PASS |
| Python | 3.8.10 | version PASS; workspace utilities/tests chạy bằng bản này |
| GNU Make | 4.2.1 | version PASS; Make targets được ghi trong report |
| CMake | 3.16.3 | version PASS; upstream firmware build NOT RUN |
| GCC / G++ host | 9.4.0 | version PASS; simulator compilation NOT RUN |
| PyYAML | 5.3.1 | import/parse PASS; CI/new env pin 6.0.2 chưa được cài/chạy tại máy này |
| Verilator | 4.028 (2020-02-06) | version PASS; compatibility với source pin NOT RUN |
| riscv64-unknown-elf-gcc | 9.3.0 | version/multilib query PASS; isolated RV32IMC object compile PASS |
| riscv32-unknown-elf-gcc / objcopy | không thấy trong PATH | BLOCKED cho build upstream yêu cầu prefix này |
| FuseSoC / Edalize | FuseSoC không thấy trong PATH; Edalize chưa cài/kiểm chứng | Build BLOCKED; có direct VCS pins |
| OpenOCD | không thấy trong PATH | Debug BLOCKED |
| GDB multiarch / riscv32-unknown-elf-gdb | không thấy trong PATH | Debug BLOCKED |
| GTKWave | không thấy trong PATH | Waveform GUI NOT RUN |
| Vivado local | không thấy trong PATH; các root cài phổ biến không có executable | Server USER-AVAILABLE; agent version/license/build NOT RUN |

`make doctor` hoàn tất inventory kể cả khi tool optional thiếu. Chỉ `make vivado-check`
có exit nonzero riêng khi Vivado chưa chạy được. Probe chỉ giữ dòng version đầu, không đọc
environment chứa license values. `VIVADO_BIN=/path/to/bin/vivado make vivado-check` hoặc source
`settings64.sh` trên server khi người dùng sẵn sàng.

Compiler smoke thực tế đã chạy trong thư mục tạm, source chỉ có hàm cộng unsigned:

```sh
riscv64-unknown-elf-gcc -march=rv32imc -mabi=ilp32 -ffreestanding -c probe.c -o probe.o
riscv64-unknown-elf-readelf -h probe.o
```

Hai lệnh exit 0; object ELF32, machine RISC-V, RVC/soft-float ABI. Chưa link firmware,
chưa kiểm tra libc/runtime, không tự tạo symlink đánh lừa prefix compiler upstream.

Nguồn install: [local setup](../docs/guides/local-setup.md) và
[official source index](../docs/references/README.md). Log kiểm tra workspace:
[validation report](../docs/reports/workspace-validation-2026-10-23.md).
