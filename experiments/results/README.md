# Run metadata

Chưa có run thực tế. Mỗi run mới có thư mục `results/<run-id>/` với `run.yaml` đã điền từ [template](../configurations/experiment-template.yaml), checksum manifest và summary nhỏ khi có kết quả.

Tracked: metadata, số liệu đã tổng hợp có đơn vị, đường dẫn và checksum artifact. Không tracked: raw logs lớn, waveform, dump, ELF/bitstream và dữ liệu radar. Vị trí raw storage phải có trong run metadata, cùng chính sách giữ/backup; checksum không thay thế bản sao lưu.

Không sửa giá trị một run cũ để hợp giả thuyết. Nếu phát hiện lỗi, thêm correction dẫn tới run mới và giữ lịch sử. Số liệu ở báo cáo/luận văn phải dẫn về run này, không tạo bộ số liệu riêng.
