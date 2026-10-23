# Upstream và tái lập

Nguồn chuẩn là [upstream.lock.json](upstream.lock.json); ngày kiểm tra 2026-10-23.
Đã đọc metadata, README, core files và vendor lock qua GitHub chính thức. Chưa clone,
cài dependency, build hay mô phỏng trong lượt khởi tạo.

| Thành phần | Revision | Vai trò |
| --- | --- | --- |
| Ibex Demo System | `d37beb753e19482eb054aefac73a27289bf72e47` | SoC và flow build chính |
| Ibex trong demo | `594ea976c9dad793f87edf91ec1c4c1df447e6dc` | Provenance của `vendor/lowrisc_ibex` |
| Demo System Labs | `5a2eec7ebd567a4ac763f4c1b971d191414ebe79` | Tài liệu học, tùy chọn |

Dùng checkout có kiểm tra URL và full commit, không dùng submodule: demo đã chứa
vendor tree và các `vendor/*.lock.hjson`, không có `.gitmodules` tại revision này.
Pin của demo cố định cả source tree, patch và license con. Ibex lock là provenance
upstream trước các patch trong demo, không phải cam kết tree hai nơi giống hệt nhau.
Không chạy vendor update hoặc thay Ibex bằng master trong baseline.

Từ root workspace:

```sh
python3 scripts/setup/upstream.py
# Chỉ khi đã sẵn sàng tải source qua mạng:
make upstream
```

Checkouts ở `third_party/checkouts/<name>` được ignore. Lệnh verify không tự tải.
`make upstream` là hành động tải chủ động; agent cần approval theo spec trước download
không nhỏ. Không ghi đè checkout dirty hay đổi remote âm thầm. Không thêm checkout Ibex
riêng vào FuseSoC core search của demo: có thể trùng VLNV.

Demo còn ghi provenance OpenTitan `d268f271f4f75aeb8f3bf9624a497ae5bfb9c47e`
và riscv-dbg `138d74bcaa90c70180c12215db3776813d2a95f2` trong vendor locks.
Giữ nguyên các license/NOTICE của từng vendor; Apache-2.0 của demo không tự áp dụng
cho mọi file con. Labs là CC-BY-4.0; chỉ liên kết và ghi nguồn, không chép nguyên bài.

[python-requirements.in](python-requirements.in) thay hai branch `ot` di động
bằng commit nguồn đã kiểm tra. Các package PyPI/transitive **chưa khóa đầy đủ** và
cặp tool này **chưa được build thử**. Sau lần cài/build thành công, lưu `pip freeze`
đã kiểm tra URL/private paths vào báo cáo môi trường; nâng pin là thay đổi riêng có
test và ADR nếu ảnh hưởng baseline. Đừng gọi môi trường hiện tại là reproducible build đã xác nhận.

Nguồn: [demo vendor tree](https://github.com/lowRISC/ibex-demo-system/tree/d37beb753e19482eb054aefac73a27289bf72e47/vendor),
[requirements gốc](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/python-requirements.txt),
[labs/license](https://github.com/lowRISC/ibex-demo-system-labs/blob/5a2eec7ebd567a4ac763f4c1b971d191414ebe79/README.md).
