# Thí nghiệm có thể tái lập

Trạng thái 2026-10-23: **chưa có experiment run hoặc measurement thực tế**. Workspace checks không được ghi thành Ibex simulation hay FPGA result. Trạng thái hệ thống hiện tại ở [current-state](../ai/current-state.md), tiêu chí kỹ thuật ở [verification matrix](../docs/verification/verification-matrix.md).

1. Copy [configuration template](configurations/experiment-template.yaml) thành cấu hình có `experiment_id`; điền câu hỏi, controls, metric, acceptance rule trước khi chạy. Board-dependent runs bị chặn đến khi board/device được quyết định.
2. Chốt source commit, upstream commits, dirty state, firmware SHA, tool versions/flags, clock/board và dataset manifest/hash. Ghi lệnh chính xác cùng working directory và exit code; không ghi secret hoặc toàn bộ environment.
3. Mỗi lần chạy có ID riêng dạng `YYYYMMDDTHHMMSSZ-short-name-nn` theo UTC. Giữ cấu hình trước chạy bất biến; copy thành `results/<run-id>/run.yaml` để ghi metadata sau chạy và hash của cấu hình gốc. Không tính hash tự tham chiếu của file chứa chính hash đó. Raw logs/waveforms/dumps lưu ở vùng ignored hoặc kho ngoài Git được ghi trong manifest.
4. Tính SHA-256 cho cấu hình, firmware và từng artifact. Ghi hash của file gốc trước khi trích/tóm tắt; nếu tạo bản đã bỏ thông tin riêng tư, ghi đó là derivative và hash riêng. Khóa run đã thu, chạy lại dùng ID mới.
5. Copy [result template](reports/result-template.md), trỏ tới run metadata và lệnh phân tích. Ghi mọi run fail/outlier và lý do loại mẫu đã đăng ký; chỉ kết luận trong phạm vi đo.

`PASS` = tiêu chí đã đặt được kiểm chứng bằng artifact; `FAIL` = đã chạy và không đạt; `BLOCKED` = chưa thể chạy vì prerequisite cụ thể; `NOT RUN` = chưa chạy. YAML dùng `NOT_RUN` để làm enum; hiển thị trong báo cáo là `NOT RUN`.

Phân loại bằng chứng: `HOST_CHECK`, `SIMULATION`, `FPGA_BUILD`, `FPGA_MEASUREMENT`, `EXTERNAL_CITATION`, `INFERENCE`. Version check, synthesis, implementation, timing closure, bitstream và chạy trên board là sáu mốc riêng. Không gọi synthesis thành công là bring-up thành công.

Tham khảo [tool versions](../tools/tool-versions.md) và [local setup](../docs/guides/local-setup.md). Không điền số giả vào mẫu để có bảng đẹp. Chưa có dataset thì dùng `null` và giải thích “not applicable” khi thật sự không liên quan.
