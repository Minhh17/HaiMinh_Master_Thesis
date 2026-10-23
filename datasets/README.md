# Dataset provenance

Trạng thái 2026-10-23: chỉ có catalog và manifest template; **không tải dataset, không có dữ liệu radar thực hoặc fixture giả làm dữ liệu đo**. Phase 1 không cần radar dataset.

- [Catalog ứng viên](catalog.md): kiểm tra nguồn, quyền sử dụng và rủi ro truy cập trước khi chọn.
- [Manifest template](manifests/dataset-template.yaml): copy thành manifest có ID và version sau khi đã chấp thuận sử dụng.
- [Samples policy](samples/README.md): chỉ nhận fixture nhỏ có quyền phân phối rõ ràng.

Raw data ở `$THESIS_DATA_ROOT` ngoài cây Git; đây là biến do người dùng chọn, không có đường dẫn mặc định ngầm. Ví dụ thiết lập trên máy cá nhân sau khi đã chọn ổ lưu:

```sh
export THESIS_DATA_ROOT="/path/to/external/thesis-data"
```

Không commit đường dẫn riêng tư của máy hoặc token vào manifest. Dùng dạng `${THESIS_DATA_ROOT}/dataset-id/version`; expansion do script tương lai thực hiện, YAML không tự expand biến. Tải chỉ sau khi đã xác minh license/restrictions, dung lượng và được người dùng cho phép.

Quy trình tiếp nhận: ghi URL/version/license → chọn subset và split theo sequence/session → tải ngoài Git → kiểm tra checksum của publisher nếu có → tự tính SHA-256 cho từng file → ghi script/commit xử lý → xác nhận shape/dtype/rate → đánh dấu trạng thái. Hash tự tính nhận diện byte đã nhận, không chứng minh tác giả hay tính xác thực nếu không có hash tin cậy để đối chiếu.

Không tự bật DVC remote hoặc Git LFS. Cân nhắc DVC khi dữ liệu lớn thực sự đến; LFS chỉ cho asset vừa phải đã chọn và kiểm tra quota. Raw data cần phương án backup riêng: Git không sao lưu dữ liệu bị ignore.
