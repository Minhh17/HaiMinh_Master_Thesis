# Vivado: từ môi trường tới báo cáo triển khai

**Vivado trên server: CONFIRMED BY USER.** Người dùng cho phép giữ placeholder;
server hostname/path/access chưa được cung cấp và agent chưa truy cập server.
Executable/version/edition/license cần được kiểm tra trên server dùng để build.
Không cần cài Vivado local chỉ để hoàn tất workspace. Board TBD; synthesis, implementation,
bitstream và hardware test **NOT RUN/BLOCKED**. Xem [tool report](../../tools/tool-versions.md).

## Kiểm tra không cần board

```sh
command -v vivado
vivado -version
make vivado-check
```

Các lệnh trên chạy ở host agent chỉ phản ánh host agent; để kiểm tra Vivado thật,
chạy chúng trên server. Nếu PATH chưa có, người dùng tìm đúng `settings64.sh` của bộ cài đã có và
`source` nó trong Bash, rồi chạy lại. Không giả định version hay cài mới.
`vivado -version` thành công không chứng minh license/device support đủ cho
target. Không commit file license, machine ID hoặc đường dẫn nội bộ vào log chia sẻ.
Nguồn cài đặt: [AMD Vivado downloads](https://www.xilinx.com/support/download.html).

## Gate board và build

Hoàn tất [ADR board](../decisions/ADR-template-board-selection.md), sau đó
`fpga/boards/selected-board.json` phải có status `approved`, board ID,
target và đường dẫn ADR tồn tại. Target phải khớp
[candidates](../../fpga/boards/candidates.json); CLI BOARD phải khớp quyết định.
Không tự dùng target mặc định `synth` khi board TBD.

Từ root, sau khi các gate đã đạt:

```sh
make fpga BOARD=<approved-board-id>
```

Wrapper dùng CMake build firmware trước rồi ủy quyền cho upstream. Lệnh thực
trong demo checkout (TARGET lấy từ quyết định, không đoán) là:

```sh
fusesoc --cores-root=. run --target="$TARGET" --setup --build lowrisc:ibex:demo_system
```

FuseSoC/Edalize sinh danh sách source, project/Tcl/Makefile và gọi Vivado cho
synthesis/implementation/bitstream. Giữ các output đó local; version hóa .core,
config và constraints provenance thay vì commit generated .xpr. XDC và device
part đến từ target trong [core file cố định](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/ibex_demo_system.core).
Trước build, review top/clock/reset/pinout cho đúng board revision; không có XDC
tự tạo trong workspace hiện tại.

## Logs và timing/resource reports

Build thường nằm dưới `third_party/checkouts/ibex-demo-system/build/lowrisc_ibex_demo_system_0/<target>-vivado/`.
Tìm file thực sau build, vì tên Tcl/run có thể đổi theo Edalize:

```sh
rg --files --hidden --no-ignore third_party/checkouts/ibex-demo-system/build -g '*.log' -g '*.rpt' -g '*.dcp' -g '*.bit' -g '*.tcl'
```

Kiểm tra `vivado.log`, synthesis/implementation run logs và exit status;
giữ cả warnings liên quan unconstrained paths, clock, DRC. Muốn tái chạy batch
synthesis/implementation, ưu tiên chính FuseSoC command ở trên hoặc Makefile
nó sinh; không tự thay source list bằng glob RTL.

Khi đã xác định **routed checkpoint** thực từ run đó, dùng batch để xuất báo cáo:

```sh
vivado -mode batch -source fpga/scripts/report_checkpoint.tcl -tclargs /absolute/path/to/routed.dcp build/vivado-reports/run-id
```

Script chỉ mở DCP và xuất timing summary/utilization/DRC/route status; không tạo
baseline hoặc PASS. Đọc WNS/TNS, hold, clock constraints, paths chưa constrain,
route status và DRC trước khi kết luận timing closure. Utilization phải ghi rõ
post-route hay post-synthesis, FPGA part, tool/source/config tương ứng.
Nguồn: [AMD báo cáo implementation](https://docs.amd.com/r/en-US/ug904-vivado-implementation/Step-8-Run-Required-Reports),
[open_checkpoint](https://docs.amd.com/r/en-US/ug904-vivado-implementation/open_checkpoint),
[timing summary](https://docs.amd.com/r/en-US/ug906-vivado-design-analysis/Report-Timing-Summary).

## Import kết quả từ máy người dùng

Trên server, dùng bản workspace cùng revision (copy/archive hoặc Git remote riêng
sau khi người dùng thiết lập); không giả định SSH hostname, tài khoản hay storage.
Các bước dưới chạy trong root workspace ở server bằng Bash; chưa có board thì
chỉ thu môi trường, không chạy `make fpga`:

```bash
mkdir -p build/validation/vivado-server
make doctor > build/validation/vivado-server/doctor.txt 2>&1
make vivado-check > build/validation/vivado-server/vivado-check.txt 2>&1
git rev-parse HEAD > build/validation/vivado-server/workspace-revision.txt
```

Nếu workspace chưa có commit, ghi trạng thái uncommitted và checksum manifest thay
cho SHA tưởng tượng. Giữ exit code thực của từng lệnh; file log tồn tại không
chứng minh thành công. Người dùng sau đó có thể copy thư mục kết quả này về cùng
`build/validation/vivado-server/` ở máy local. Không cần agent tự truy cập server.

Sau khi tools/source/board gate đã đạt, ghi phiên build trên server:

```bash
set -o pipefail
make fpga BOARD=<approved-board-id> 2>&1 | tee build/validation/vivado-server/fpga-build.log
```

Điền board thật trước khi chạy, kiểm tra exit status ngay khi lệnh kết thúc,
lưu logs/reports/bitstream checksum rồi tạo run manifest. Dùng run-id mới cho
mỗi lần đo; không ghi đè bằng chứng cũ. Việc program board phụ thuộc vị trí
board/JTAG và quyền truy cập, còn **TBD**, tách khỏi build trên server.

Output nặng/log nguyên ở server build hoặc ignored `build/`; chuyển bản tóm tắt
đã loại thông tin riêng tư vào `fpga/reports/<run-id>.md`. Ghi command,
source pin, firmware hash, versions, board/part/clock, thời điểm, raw file
locations+SHA-256 và observed result; dùng [report template](../../fpga/reports/README.md).
Build bitstream thành công là bằng chứng build. UART/GPIO/timer/JTAG trên board
cần [bring-up](fpga-bringup.md) riêng; không nhập số giả để lấp bảng.
