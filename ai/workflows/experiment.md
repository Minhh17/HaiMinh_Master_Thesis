# Experiment workflow

Dùng [experiments](../../experiments/README.md). Trước run: khóa câu hỏi, baseline, input,
variables, số lần lặp, tiêu chí loại run và acceptance criteria. Ghi revision của workspace,
upstream, tool versions, flags, board/clock/reset, firmware và dataset checksums.

Chạy chính xác command đã ghi; lưu stdout/stderr/raw ở ignored storage, compact results trong
Git. Không sửa raw để khớp kỳ vọng. Phân biệt simulation/FPGA/analytic inference. Run fail hoặc
bị chặn vẫn có record, không đưa số “0” thay cho missing measurement.

Sau run: phân tích controls, uncertainty và limitations; nối requirement/task/test/experiment/
report; cập nhật matrix chỉ theo bằng chứng. Handoff phải đủ cho người khác chạy lại.
