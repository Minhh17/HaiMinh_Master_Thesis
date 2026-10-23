# ADR-0001 — Workspace Git độc lập và checkout upstream có pin

- Ngày: 2026-10-23
- Trạng thái: ACCEPTED cho tổ chức workspace
- Phạm vi: hạ tầng cá nhân; không chọn license phát hành hay tạo GitHub remote

**Bối cảnh.** Thư mục cha chứa spec người dùng và `.git` được môi trường bảo vệ.
Cần một root hoàn chỉnh tên `riscv-ibex-thesis` mà không sửa index/config của repo cha.
Source RTL tham chiếu có vòng đời và license riêng.

**Quyết định.** Tạo root con `Master_Thesis/riscv-ibex-thesis/` với Git metadata
của chính nó khi môi trường cho phép; mọi lệnh trong README bắt đầu tại root con.
Giữ nguyên spec/attachment và `.git` cha. Không đăng ký repo con thành submodule cha,
không push hay tạo public remote. Tách notes, research evidence, implementation,
experiment runs và thesis theo một nguồn chuẩn cho từng loại.

Upstream dùng repeatable checkout script + full SHA + URL, clone tại
`third_party/checkouts/` được ignore. Demo đã mang vendor tree cùng locks;
dùng chính dependency model đó. Không vendor lại RTL vào `hardware/`.
Các file nặng/generated/private ở ngoài Git hoặc dưới ignored output.

**Lựa chọn đã cân nhắc.** Sửa trực tiếp repo cha đơn giản hơn nhưng ảnh hưởng dữ
liệu bàn giao và metadata được bảo vệ. Submodule là phương án hợp lệ khi repo
cha đã quản lý dependency chuẩn; tại đây checkout script tách acquisition khỏi
việc khởi tạo workspace và cho chẩn đoán offline. Archive copy làm mất lịch sử
và dễ mất provenance nên không chọn.

**Hệ quả.** Người dùng cần `cd riscv-ibex-thesis` trước Git; status của cha
không thay status repo con. Lock chưa tương đương build đã kiểm chứng. Dependency
update phải có diff pin và rerun test; không có tải source ngầm trong `make check`.

Tham chiếu: [third_party](../../third_party/README.md),
[scope](../design/phase1-scope.md).
