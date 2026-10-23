PYTHON ?= python3
BOARD ?=

.PHONY: help doctor vivado-check check test upstream sim fpga
help:
	@$(PYTHON) scripts/maintenance/help.py

doctor:
	@$(PYTHON) scripts/setup/doctor.py

vivado-check:
	@$(PYTHON) scripts/setup/doctor.py --vivado-only

check:
	@$(PYTHON) scripts/maintenance/validate_workspace.py
	@$(PYTHON) -m unittest discover -s scripts/test -p 'test_*.py' -v

test:
	@$(PYTHON) -m unittest discover -s scripts/test -p 'test_*.py' -v

upstream:
	@$(PYTHON) scripts/setup/upstream.py --fetch

sim:
	@$(PYTHON) scripts/build/run.py sim

fpga:
	@$(PYTHON) scripts/build/run.py fpga --board "$(BOARD)"
