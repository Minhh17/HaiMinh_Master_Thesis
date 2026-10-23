# DSP — future scope

Trạng thái: **DEFERRED, Phase 2 trở đi**. Phase 1 chỉ bring-up SoC, firmware, ngoại vi và debug. Chưa có thuật toán DSP, custom instruction, MMIO accelerator, ADC/RF chain hoặc ứng dụng radar được triển khai.

Khi mở Phase 2, bổ sung từng thư mục khi có nội dung thực:

| Vùng dự kiến | Hợp đồng cần có |
|---|---|
| `algorithms/` | Mô tả toán học, shape và đơn vị, normalization, boundary cases |
| `python-reference/` | Reference dễ đọc; pinned dependencies; tests độc lập và sai số cho phép |
| `matlab-reference/` | Chỉ dùng nếu có nhu cầu và quyền sử dụng; ghi toolbox/version |
| `benchmarks/` | Kernel chuẩn C/RISC-V, compiler/flags, correctness oracle, timer overhead |

Trước tối ưu phải chốt định dạng số, rounding/saturation, layout, stride, tolerances và input hash. Kiểm tra impulse/constant/small hand-computable cases khi phù hợp; không chỉ so implementation với chính nó. Báo cả compute-only và end-to-end nếu có transfer/setup.

Kernel và dữ liệu chỉ chọn sau [RQ-01](../research/research-questions.md), [dataset provenance](../datasets/README.md) và baseline Phase 1. Kết quả đo lưu trong [experiments](../experiments/README.md), không lưu trùng ở đây.
