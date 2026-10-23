# Mô phỏng baseline

Trạng thái khởi tạo: **NOT RUN**. Lệnh đã đối chiếu source upstream, chưa có
bằng chứng compile hoặc chạy Ibex tại workspace.

Điều kiện: checkout đúng lock, Python environment có FuseSoC/Edalize,
Verilator + C++ + libelf, CMake, GCC prefix RV32 upstream và srecord.
Từ root workspace:

```sh
make doctor
make sim
```

`make sim` build firmware và simulator; không tự chạy ứng dụng tương tác.
Để kiểm tra độc lập, các lệnh tương đương trong checkout là:

```sh
cd third_party/checkouts/ibex-demo-system
cmake -S sw/c -B sw/c/build
cmake --build sw/c/build
fusesoc --cores-root=. run --target=sim --tool=verilator --setup --build lowrisc:ibex:demo_system
./build/lowrisc_ibex_demo_system_0/sim-verilator/Vtop_verilator --meminit=ram,./sw/c/build/demo/hello_world/demo
```

README nói “Ibex repository root” ở đoạn simulation nhưng core cần dùng là
demo_system, vì vậy cwd ở trên là **demo checkout**. Labs cũ dùng `sw/build`;
pin hiện tại dùng `sw/c/build`. Không thay đường dẫn vì FPGA core có default
`blank.vmem` phụ thuộc vị trí đó.

Hello-world ở pin hiện tại chạy vòng lặp với timer, UART và `wfi`; không phải
self-checking test có exit PASS. UART DPI có thể in đường dẫn pseudo-terminal;
mở terminal đúng đường dẫn simulator thông báo để đọc UART. Có thể thêm `-t`
để tạo FST rồi mở bằng GTKWave. Không đoán tên FST; tìm file thực trong cwd/build.

Có thể chủ động giới hạn phiên quan sát (Linux GNU timeout):

```sh
timeout --signal=INT 30s ./build/lowrisc_ibex_demo_system_0/sim-verilator/Vtop_verilator -t --meminit=ram,./sw/c/build/demo/hello_world/demo
```

Exit 124 nghĩa timeout, không tự xem là PASS hoặc lỗi CPU. Ghi lý do dừng,
stdout/stderr và UART riêng; `ibex_demo_system.log` thuộc simulation-control
peripheral có thể không chứa UART output mặc định. Nếu bật
`-DSIM_CTRL_OUTPUT=ON` ở CMake, ghi config khác baseline và rebuild.

Tiêu chí quan sát đầu tiên: ELF được nạp đúng, thấy PC hoạt động và output
hello-world/timer đúng source, không có lỗi simulator; sau đó viết test
self-checking để đạt gate ở [verification matrix](../verification/verification-matrix.md).
Lưu source/ELF hashes, versions, lệnh đầy đủ, thời gian, trạng thái, log location
trong run manifest. Waveform/raw log giữ ngoài Git; report ngắn có link/checksum.

Nguồn: [build/run upstream](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md),
[hello_world/main.c](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/sw/c/demo/hello_world/main.c),
[CMake option](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/sw/c/CMakeLists.txt).
