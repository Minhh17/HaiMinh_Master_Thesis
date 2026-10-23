# Catalog dataset ứng viên

Kiểm tra tài liệu web ngày **2026-10-23**. `DOCUMENTATION CHECKED` chỉ có nghĩa đã đọc nguồn; quyền tải, khả năng tải đủ archive, cấu trúc byte và checksums đều chưa được kiểm chứng trên file. Không tải dữ liệu trong đợt tạo workspace.

| ID | Nguồn chính thức và dữ liệu được mô tả | Truy cập và license | Gate trước khi dùng |
|---|---|---|---|
| `gao-ti77-adc-automotive` | [Repository của Xiangyu Gao](https://github.com/Xiangyu-Gao/Raw_ADC_radar_dataset_for_automotive_object_detection): TI AWR1843, 2 TX/4 RX; ADC `.mat`, các trục sample/chirp/RX/TX = 128/255/4/2. [IEEE DataPort DOI](https://doi.org/10.21227/xm40-jx59). | README có Google Drive và DataPort; ghi đã sửa Drive link tháng 5/2025. [LICENSE](https://github.com/Xiangyu-Gao/Raw_ADC_radar_dataset_for_automotive_object_detection/blob/main/LICENSE) là MIT cho software; README cũng nói license của tool. **Không suy rộng MIT cho raw data.** DataPort bị robots chặn trong công cụ duyệt; chưa kiểm tra quyền truy cập archive. | Xác nhận license riêng của dữ liệu, version và dung lượng; làm rõ dtype/bit width/sample rate từ cấu hình và file; kiểm tra checksum. |
| `radial-raw` | [Repository valeoai/RADIal](https://github.com/valeoai/RADIal): dữ liệu ADC binary từ 4 radar chips, 16 RX/12 TX; cung cấp DBReader và SignalProcessing. Cần phân biệt raw ADC với gói “ready to use” đã xử lý. | README thông báo dữ liệu khả dụng trở lại trong 2024 và có [download landing link](https://linkly.link/2EakA). Link chuyển tới Google Drive nhưng công cụ duyệt không đọc được folder. Không tìm thấy điều khoản cấp phép dataset trong README đã xem; **LICENSE UNVERIFIED**. | Đọc điều khoản tại nơi phân phối hoặc xác nhận từ chủ sở hữu; chọn raw subset, kiểm tra schema/calibration và checksums; ghi rõ processing trước khi benchmark. |

Hai ứng viên đều ở trạng thái **CANDIDATE / NOT DOWNLOADED / NOT VALIDATED**. Đây không phải khuyến nghị chọn dataset cuối cùng. Giá trị shape/hardware ở bảng là mô tả từ nguồn bên ngoài, không phải đo đạc của luận văn. Chưa ghi sample rate, dtype hoặc bit width vì chưa xác minh trực tiếp đủ căn cứ.

Nguồn kiểm tra thêm cho RADIal: [DBReader](https://github.com/valeoai/RADIal/blob/main/DBReader/README.md), [SignalProcessing](https://github.com/valeoai/RADIal/blob/main/SignalProcessing/README.md). Các thư viện này chưa được cài hoặc chạy trong workspace.

Để tiếp tục: quyết định workload sau Phase 1 → chọn ứng viên và subset tối thiểu → hoàn thiện [manifest](manifests/dataset-template.yaml) → xác nhận quyền tải và lưu ngoài Git → kiểm chứng dữ liệu trước khi gắn vào thí nghiệm. Việc dữ liệu được quảng bá là public không đủ để kết luận quyền tái phân phối.
