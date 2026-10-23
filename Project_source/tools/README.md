# Công cụ và môi trường

[Tool inventory](tool-versions.md) phân biệt available-to-user, executable detected và actual test.
Kiểm kê lại bằng `make doctor`; lưu JSON với:

```sh
python3 scripts/setup/doctor.py --json build/validation/doctor.json
```

Workspace checks dùng Python ≥3.8, Git và PyYAML. `requirements-check.txt` pin phiên bản cho
môi trường mới/CI; máy bootstrap đang có PyYAML 5.3.1 và đã chạy validation với phiên bản đó.
Tool build upstream theo [local setup](../docs/guides/local-setup.md) và
[source pins](../third_party/README.md). Chưa có fully resolved Python build lock hoặc toolchain
container đã kiểm chứng; ghi môi trường thực trước baseline thay vì tự gắn nhãn reproducible build.

Vivado ở server của người dùng, không cài trong workspace. Local scripts hỗ trợ diagnostic
và delegate flow upstream sau khi có environment/board. Xem [server runbook](../docs/guides/vivado-workflow.md).
Không lưu license, đường dẫn private host hoặc credentials vào báo cáo tracked.
