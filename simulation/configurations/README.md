# Cấu hình simulation

Baseline: demo pin trong upstream.lock.json, FuseSoC target sim, Verilator,
core mặc định và ELF từ sw/c/build. Manifest run cần thêm tool versions,
firmware flags/hash, SIM_CTRL_OUTPUT, tracing và thời gian dừng.
Không ghi cycle count hoặc PASS trước khi chạy.
