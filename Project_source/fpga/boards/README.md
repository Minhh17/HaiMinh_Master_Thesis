# FPGA candidates — chưa quyết định

**TBD** trong [selected-board.json](selected-board.json).
Bảng lấy từ README và core file demo pin ngày 2026-10-23; không xác nhận tồn kho,
giá, license hoặc kết quả build của luận văn.

| Board ID | Board | Target | Upstream mô tả |
| --- | --- | --- | --- |
| arty-a7-35t | Digilent Arty A7-35T | synth | Good support |
| sonata | NewAE Sonata | synth_sonata | Good support |
| arty-s7-25t | Digilent Arty S7-25T | synth_artys7-25 | Community/experimental |
| arty-s7-50t | Digilent Arty S7-50T | synth_artys7-50 | Community/experimental |
| nexys-a7-100t | Digilent Nexys A7-100T | synth_nexysa7 | Community/experimental |
| blackboard | RealDigital Blackboard | synth_blackboard | Community/experimental |
| boolean | RealDigital Boolean | synth_boolean | Community/experimental |
| cw305-a100 | NewAE CW305-A100 | synth_cw305 | Community/experimental |
| cw312t-xc7a35 | NewAE CW312T-XC7A35 | synth_cw312a35 | Community/experimental |

[JSON mapping](candidates.json) cho tool. Chọn theo khả năng tiếp cận board,
đúng part/revision/XDC, Vivado/device support, UART/JTAG/GPIO và headroom có căn cứ.
Blackboard UART trong demo đi qua PMODC, cần đánh giá adapter phù hợp;
không suy UART qua USB onboard luôn dùng được.

Dùng [ADR template](../../docs/decisions/ADR-template-board-selection.md), ghi quyết định,
sau đó status=approved, board/target khớp bảng và adr trỏ tới file quyết định.
Không dùng các giá trị trong bảng như lựa chọn ngầm.
Nguồn: [README](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/README.md),
[core targets](https://github.com/lowRISC/ibex-demo-system/blob/d37beb753e19482eb054aefac73a27289bf72e47/ibex_demo_system.core).
