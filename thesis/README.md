# Luận văn

Trạng thái: đề cương **PROVISIONAL**, chưa có chương kết quả. Viết bằng tiếng Việt, giữ thuật ngữ kỹ thuật khi cần. [Đề cương](outline/outline.md) định nghĩa câu hỏi mỗi chương; [claim-to-evidence.csv](claim-to-evidence.csv) là chỉ mục truy vết, hiện chỉ có header vì chưa có claim đã được kiểm chứng.

Chuỗi truy vết: requirement → work item → ADR → implementation revision → test ID → experiment/run ID → artifact hash → claim → bảng/hình/đoạn luận văn. Thiếu mắt xích phải ghi giới hạn, không tự điền bằng suy đoán.

| Thành phần | Quy tắc |
|---|---|
| [Chapters](chapters/README.md) | Mỗi khẳng định kỹ thuật có citation hoặc claim ID; phân biệt kết quả với kế hoạch |
| [Figures](figures/README.md) | Hình tự sinh có script, data/run IDs và units; hình trích có quyền sử dụng |
| [Bibliography](bibliography/README.md) | Dùng bibliography chung, không giữ bản sao chỉnh sửa độc lập |

Trạng thái một claim: `PROVISIONAL`, `SUPPORTED`, `REFUTED`, `LIMITED`. Chỉ `SUPPORTED` khi bằng chứng đủ trong phạm vi phát biểu; kết quả âm vẫn có giá trị. Không kết luận Ibex tối ưu, có novelty hoặc đạt performance khi chưa so sánh/đo.
