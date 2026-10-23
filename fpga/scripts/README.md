# Tcl hỗ trợ báo cáo

[report_checkpoint.tcl](report_checkpoint.tcl) nhận DCP và output directory mới,
mở thiết kế rồi xuất timing/utilization/DRC/route-status. Script không build,
không program, không tự kết luận PASS. Chưa chạy Vivado trong phiên khởi tạo.
Flow build vẫn là FuseSoC/Edalize upstream; xem [Vivado workflow](../../docs/guides/vivado-workflow.md).
