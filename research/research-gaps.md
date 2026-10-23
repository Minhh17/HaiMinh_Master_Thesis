# Gap register — PROVISIONAL

Trạng thái 2026-10-23: **chưa xác lập research gap**. Một điểm chưa hiểu hoặc chưa tìm được bài không phải bằng chứng rằng chưa ai làm.

| Candidate | Cần tìm và đối chiếu | Bằng chứng hiện có | Trạng thái |
|---|---|---|---|
| G-01: so sánh custom instruction và MMIO trên workload/budget giống nhau | Primary papers, baseline, transfer overhead, tần số, độ chính xác số | Chưa review toàn văn | PROVISIONAL |
| G-02: tối ưu data movement cho kernel có bottleneck thực | Các phép đo end-to-end, bus/memory architecture, ablation | Chưa profile baseline | PROVISIONAL |

Mỗi đợt tìm kiếm ghi ngày, kho tìm kiếm, nguyên văn truy vấn, bộ lọc, tiêu chí chọn/loại và paper IDs trong note. Truy vấn khởi đầu: `RISC-V custom instruction memory mapped accelerator DSP comparison`, `RISC-V radar FFT data movement FPGA`. Chúng là kế hoạch tìm kiếm, không là kết quả khảo sát.

Chỉ nâng một gap thành `EVIDENCE-SUPPORTED` khi có ma trận công trình liên quan, đã đọc phương pháp/kết quả, chỉ rõ phần chưa giải quyết trong phạm vi cụ thể, và người học xác nhận. Lưu cả bằng chứng phản bác gap. Liên kết tới [literature matrix](literature/literature-matrix.csv) và [paper template](literature/papers/paper-template.md); không lập danh sách bài giả.
