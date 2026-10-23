# Documentation workflow

Chọn đúng nơi: explanation người học → knowledge; paper/hypothesis → research; implementation
và interface → docs; measurement → experiments; luận điểm → thesis. Dẫn nguồn canonical thay
vì copy trạng thái vào nhiều bảng. Mọi tài liệu có scope/verification state rõ ràng.

Đối chiếu command và source pin trước sửa guide, cập nhật ADR khi quyết định đổi. Chạy
`make check` để kiểm tra file links/config. Kiểm tra thủ công heading anchors, rendered Mermaid,
external URLs và citation vì validator offline không chứng minh các phần đó. Kết thúc cập nhật
state/handoff với điều thật sự kiểm chứng; không ghi phần mô tả mới thành tính năng đã chạy.
