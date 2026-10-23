"""Keep quickstart commands usable without optional dependencies."""
print('''Ibex thesis workspace (run from repository root)
  make doctor         Inventory tools; missing optional tools reported BLOCKED
  make vivado-check   Execute Vivado version check; exit nonzero if unavailable
  make check          Structure, links, configuration, hygiene + utility tests
  make test           Utility regression tests only
  make upstream       NETWORK: acquire locked upstream after download approval
  make sim            Build firmware and upstream simulator; NOT a runtime test
  make fpga BOARD=id  Board-approved upstream FPGA build; requires recorded ADR

Start: README.md -> planning/weekly/week-01.md -> ai/next-actions.md
No target installs proprietary tools or publishes to GitHub.''')
