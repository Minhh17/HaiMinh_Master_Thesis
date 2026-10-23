# FPGA baseline

Board **TBD**; chưa có synthesis/implementation/bitstream/hardware validation.
Nguồn quyết định máy đọc là [selected-board.json](boards/selected-board.json),
chỉ approve sau ADR thực. [Candidates](boards/README.md) là support upstream,
không phải khuyến nghị mua.

Chạy `make vivado-check` không cần board; build có gate
`make fpga BOARD=<approved-id>`. [Vivado workflow](../docs/guides/vivado-workflow.md)
giải thích source/constraints, batch và reports; [bring-up](../docs/guides/fpga-bringup.md)
tách programming và hardware tests. Generated artifacts không vào Git.
