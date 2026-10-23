# Simulation

Dùng FuseSoC target `sim` với Verilator của demo pin; xem
[runbook](../docs/guides/simulation.md). `make sim` build firmware+simulator,
không tự chạy hello-world vô hạn. Hiện NOT RUN.

Testbench riêng chỉ xuất hiện khi có module riêng. Cấu hình và tiêu chí PASS
phải version hóa; executable, waves và raw logs giữ ở ignored build/output.
