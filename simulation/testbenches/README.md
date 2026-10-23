# Testbench

Chưa có DUT riêng nên không tạo testbench rỗng. Baseline dùng
`dv/verilator/top_verilator.sv` upstream. Khi bổ sung RTL, cần stimulus,
assertions/scoreboard, reset/error cases và timeout; chạy simulator không lỗi
không thay thế kiểm tra output.
