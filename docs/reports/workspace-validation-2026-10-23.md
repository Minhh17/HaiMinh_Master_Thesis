# Workspace validation — 2026-10-23

Phạm vi: khung workspace local, Python 3.8.10/PyYAML 5.3.1. Lệnh chạy từ repo root.

`make help`, `make doctor`, `make check`: PASS ở phạm vi tương ứng. Các diagnostic exit 2 bên dưới là BLOCKED đúng prerequisite; không có build hay hardware test.

Vivado **CONFIRMED BY USER — trên server**; local agent chưa kiểm chứng server. Không tải upstream hoặc dataset, không cài toolchain, không push.

Compiler probe riêng: `riscv64-unknown-elf-gcc -march=rv32imc -mabi=ilp32 -ffreestanding -c probe.c -o probe.o` và `riscv64-unknown-elf-readelf -h probe.o` đều exit 0. Object ELF32/RISC-V/RVC; không phải upstream firmware test.

## Output lệnh thực tế

### `make help` — exit 0

```text
Ibex thesis workspace (run from repository root)
  make doctor         Inventory tools; missing optional tools reported BLOCKED
  make vivado-check   Execute Vivado version check; exit nonzero if unavailable
  make check          Structure, links, configuration, hygiene + utility tests
  make test           Utility regression tests only
  make upstream       NETWORK: acquire locked upstream after download approval
  make sim            Build firmware and upstream simulator; NOT a runtime test
  make fpga BOARD=id  Board-approved upstream FPGA build; requires recorded ADR

Start: README.md -> planning/weekly/week-01.md -> ai/next-actions.md
No target installs proprietary tools or publishes to GitHub.
```

### `make doctor` — exit 0

```text
PASS: git: git version 2.25.1
PASS: python3: Python 3.8.10
PASS: make: GNU Make 4.2.1
PASS: cmake: cmake version 3.16.3
PASS: gcc: gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
PASS: g++: g++ (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
BLOCKED: fusesoc: not found on PATH
PASS: verilator: Verilator 4.028 2020-02-06 rev v4.026-92-g890cecc1
BLOCKED: riscv32-unknown-elf-gcc: not found on PATH
PASS: riscv64-unknown-elf-gcc: riscv64-unknown-elf-gcc () 9.3.0
BLOCKED: openocd: not found on PATH
BLOCKED: gdb-multiarch: not found on PATH
BLOCKED: riscv32-unknown-elf-gdb: not found on PATH
BLOCKED: gtkwave: not found on PATH
BLOCKED: vivado: USER-AVAILABLE / AGENT-NOT-VERIFIED; not found on PATH
Version detection does not verify tool compatibility, license, build or hardware.
```

### `make check` — exit 0

```text
PASS: 39 required files; 116 source files; local Markdown file links; JSON/YAML;
      literature CSV; 34 ignore/track cases; size/key/index hygiene.
Scope: offline workspace checks; no external URL, citation, RTL, FPGA or CI-service execution claim.
test_board_target_and_adr_must_match (test_utilities.Diagnostics) ... ok
test_documentation_cannot_link_outside_repository (test_utilities.Diagnostics) ... ok
test_malformed_lock_is_diagnostic_not_traceback (test_utilities.Diagnostics) ... ok
test_missing_tool_does_not_pass (test_utilities.Diagnostics) ... ok
test_mutable_python_pin_and_incomplete_template_fail (test_utilities.Diagnostics) ... ok
test_nonzero_version_is_failure (test_utilities.Diagnostics) ... ok
test_real_gitignore_protects_artifacts_and_keeps_sources (test_utilities.Diagnostics) ... ok
test_relative_links_and_missing_link (test_utilities.Diagnostics) ... ok
test_tbd_board_never_builds (test_utilities.Diagnostics) ... ok
test_timeout_is_blocked (test_utilities.Diagnostics) ... ok
test_upstream_preserves_dirty_sources (test_utilities.Diagnostics) ... ok
test_upstream_rejects_changed_remote_or_revision (test_utilities.Diagnostics) ... ok
test_upstream_rejects_untracked_core_injection (test_utilities.Diagnostics) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.075s

OK
```

### `make vivado-check` — exit 2

```text
BLOCKED: vivado: USER-AVAILABLE / AGENT-NOT-VERIFIED; not found on PATH
Version detection does not verify tool compatibility, license, build or hardware.
make: *** [Makefile:12: vivado-check] Error 2
```

### `make sim` — exit 2

```text
BLOCKED: upstream checkout absent: review third_party/README.md, then make upstream with download approval
BLOCKED: missing executable: fusesoc
BLOCKED: missing executable: riscv32-unknown-elf-gcc
BLOCKED: missing executable: riscv32-unknown-elf-objcopy
NOT RUN: firmware, simulation/FPGA build and hardware validation.
make: *** [Makefile:25: sim] Error 2
```

### `make fpga` — exit 2

```text
BLOCKED: board TBD: record an approved board ADR and selected-board.json; then pass BOARD=<id>
BLOCKED: upstream checkout absent: review third_party/README.md, then make upstream with download approval
BLOCKED: missing executable: fusesoc
BLOCKED: missing executable: riscv32-unknown-elf-gcc
BLOCKED: missing executable: riscv32-unknown-elf-objcopy
BLOCKED: missing executable: vivado
NOT RUN: firmware, simulation/FPGA build and hardware validation.
make: *** [Makefile:28: fpga] Error 2
```

### `python3 scripts/setup/upstream.py` — exit 2

```text
BLOCKED: upstream checkout absent: review third_party/README.md, then make upstream with download approval
```

## Giới hạn

Không chạy GitHub-hosted CI, Vivado Tcl, upstream build, simulator runtime, FPGA timing/bitstream hoặc physical tests. Link check xét đường dẫn file Markdown, không kiểm tra mọi anchor/URL ngoài. Original spec giữ nguyên; source pins xem [upstream lock](../../third_party/upstream.lock.json).
