# IBEX THESIS WORKSPACE — IMPLEMENTATION SPECIFICATION

**Status:** Handoff specification for ChatGPT Work / coding agent  
**Version:** 1.1 — 2026-10-22 (Vivado availability confirmed; handoff link refreshed)  
**Repository working name:** `riscv-ibex-thesis`  
**Language:** Vietnamese for personal learning notes, planning and thesis drafts; English technical terms, code, identifiers, standard interface specifications, bibliographic fields and commit conventions as appropriate.  
**Ownership:** Personal master's thesis workspace; intended to be private at first.

> **Environment clarification (v1.1):** The user can use Vivado. GPT Work should prepare and, where execution access permits, validate the Vivado workflow. The FPGA board is still undecided; Vivado availability is not evidence that any FPGA build or board test has passed.

## 1. Mission and operating context

Build a **real, usable, maintainable, Git-first, AI-agent-friendly research and engineering workspace** covering the full master's thesis lifecycle: learning, RISC-V SoC/FPGA implementation, firmware, peripheral experiments, DSP benchmark/reference models, dataset provenance, architectural exploration, verification, literature review, paper writing, and the final thesis.

This is an actual repository creation and validation task, **not just a proposed directory tree or a project-management essay**. Make reasonable defaults, execute supported setup/verification, and report blockers honestly.

### Current confirmed scope

- Field: Master's thesis, Computer Engineering; research direction: RISC-V/FPGA system architecture and possible accelerator integration/data-movement optimization on representative radar-DSP workloads.
- **Phase 1:** bring up a minimal **Ibex** RISC-V SoC on real FPGA hardware, run bare-metal C firmware, use UART/GPIO/timer/interrupt and OpenOCD/GDB, document/characterize the hardware baseline.
- Core preference: **lowRISC Ibex**. Reference SoC: **lowRISC Ibex Demo System**. Core and FPGA board choices are **not final**; Ibex is a preferred candidate, not a validated 'optimal' choice.
- Timeline proposal: Phase 1 spans approximately 6–8 weeks beginning 2026-10-21; weekly milestones are planning targets, not guaranteed outcomes.
- **Available to the user:** AMD/Xilinx **Vivado** (user can use it for synthesis, implementation, bitstream generation, timing analysis and FPGA debugging as supported). **Exact version/edition, license status and host execution path have not yet been recorded; the implementing agent must detect/document them rather than guess.** Vivado being available to the user does **not** guarantee the GPT Work runtime can execute it.
- Other tools to verify/setup: Ubuntu/Linux or applicable WSL2, Git, Python, SystemVerilog, FuseSoC/Edalize, Verilator, RISC-V GCC, CMake, OpenOCD/GDB and waveform viewer (e.g., GTKWave).
- Key technical references:
  - https://github.com/lowRISC/ibex
  - https://github.com/lowRISC/ibex-demo-system
  - https://github.com/lowRISC/ibex-demo-system-labs
  - https://ibex-core.readthedocs.io/
- **Do not implement custom DSP instructions, MMIO accelerators, ADC/RF chains, or radar applications in Phase 1.** Prepare extensible organization for future phases without building premature complexity.
- **Do not purchase or silently select an FPGA**. Treat board as TBD. Arty A7-35T is a plausible supported target for the reference demo; record others and board selection criteria; check current official docs before claiming board support.

### Long-term phases (future scaffolding, not active implementations)

- Phase 2: benchmark standard RISC-V software on DSP/radar-inspired kernels with reference models and controlled datasets.
- Phase 3: compare custom-instruction/tightly coupled execution and MMIO/loosely coupled accelerator where justified.
- Phase 4: identify a narrow bottleneck and a falsifiable architecture contribution with defensible experimental comparisons and literature gap analysis.
- Phase 5: thesis and paper writing. Do not claim novelty or performance without primary-source checking and measurements.

## 2. Design principles

1. **Single source of truth** for code, decisions, task status, and documentation: one central Git repository; separate heavy datasets and vendor toolchains.
2. **Useful before comprehensive:** build the Phase 1 operational workspace first; future-phase directories can have a clear README but must not be stuffed with placeholder outputs.
3. **Traceability:** link requirement → work item → design decision (ADR) → implementation → test → experiment → report.
4. **Reproducibility:** pin external dependencies (upstream URL and tested commit/tag); capture tool versions, environment, board configuration, exact commands, build flags, relevant firmware revision, results and checksums.
5. **Safety and privacy:** never commit GitHub credentials, tokens, SSH keys, company/internal radar data, confidential designs, license files, machine-specific IDs or proprietary papers without permission.
6. **Scientific integrity:** clearly distinguish hypothesis, simulation, FPGA hardware measurement, inference and external citation. Do not fabricate test outcomes, bibliographic facts or FPGA resource figures.
7. **Agent accessibility:** concise root `AGENTS.md` with project invariants and pointers to deeper documents; explicit current-state and handoff files; runnable checks.
8. **No needless infrastructure:** skip Kubernetes, databases, elaborate microservices, dashboards, heavyweight CI requiring licensed FPGA tools, premature dataset infrastructure, or multiple source-of-truth task systems.
9. **Portable local-first workflow:** use POSIX-friendly scripts and relative paths; prefer documented Ubuntu/Linux environment. **Vivado is available to the user;** detect version/path/environment on the host accessible to the agent before running any Vivado command, and report when only the user’s local environment can execute it.
10. **Academic IP/licensing:** retain attribution and licenses of upstream cores; do not vendor source or copyrighted PDF content casually; own repository license must be consciously chosen, not assumed.

## 3. Proposed repository structure

The structure is a target map. Create directories with actual useful files or a short scoped README, avoid empty scaffolding and duplicates.

```text
riscv-ibex-thesis/
├── README.md
├── AGENTS.md
├── Makefile
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .github/
│   ├── workflows/                  # tool-independent CI
│   ├── ISSUE_TEMPLATE/             # experiment, bug, task, reading
│   └── pull_request_template.md
├── planning/
│   ├── README.md
│   ├── roadmap.md
│   ├── phase1-plan.md
│   ├── backlog.md
│   ├── milestones.md
│   ├── weekly/                     # Week-01.md template + actual W1
│   └── templates/
├── knowledge/
│   ├── README.md
│   ├── computer-architecture/
│   ├── riscv-isa/
│   ├── ibex-microarchitecture/
│   ├── fpga-design/
│   ├── soc-and-buses/
│   ├── embedded-software/
│   ├── dsp/
│   └── learning-journal/
├── research/
│   ├── README.md
│   ├── research-questions.md
│   ├── hypotheses.md
│   ├── research-gaps.md
│   ├── literature/
│   │   ├── README.md
│   │   ├── literature-matrix.csv
│   │   ├── references.bib
│   │   └── papers/                 # *notes*, not copyrighted PDF copies
│   ├── experiments/
│   └── publications/
├── docs/
│   ├── architecture/              # diagrams and CPU/SoC explanations
│   ├── design/                    # specs incl. memory map, interfaces
│   ├── decisions/                 # ADRs with alternatives and evidence
│   ├── guides/                    # setup, simulate, build, debug
│   ├── verification/              # verification matrix, test cases
│   ├── reports/                   # results and Phase 1 review
│   └── references/                # link index, official sources
├── hardware/
│   ├── rtl/                       # OWN RTL (not copies of upstream)
│   ├── ip/
│   ├── constraints/
│   └── integration/
├── firmware/
│   ├── apps/
│   ├── drivers/
│   ├── tests/
│   └── common/
├── simulation/
│   ├── testbenches/
│   ├── configurations/
│   └── tests/
├── fpga/
│   ├── boards/                    # TBD until board decision
│   ├── scripts/
│   └── reports/                   # compact tracked reports only
├── dsp/
│   ├── algorithms/
│   ├── python-reference/
│   ├── matlab-reference/
│   └── benchmarks/
├── datasets/
│   ├── README.md
│   ├── catalog.md
│   ├── manifests/
│   └── samples/                   # only tiny public/synthetic fixtures
├── experiments/
│   ├── README.md
│   ├── configurations/
│   ├── results/                   # metadata/summary tracked, raw ignored
│   ├── analysis/
│   └── reports/
├── third_party/
│   └── README.md                  # upstream acquisition, SHA/license
├── scripts/
│   ├── setup/
│   ├── build/
│   ├── test/
│   └── maintenance/
├── tools/
│   └── README.md
├── ai/
│   ├── README.md
│   ├── project-context.md
│   ├── current-state.md
│   ├── next-actions.md
│   ├── workflows/
│   └── templates/                # research, learning, dev, handoff
└── thesis/
    ├── outline/
    ├── chapters/
    ├── figures/
    └── bibliography/
```

### Important distinctions

- `knowledge/` = learner-curated explanations, concepts, diagrams, exercises, understanding status. Flag AI-assisted summaries as **not yet verified by learner**.
- `research/` = external scholarly evidence, annotated papers, literature matrix, research questions, gaps, assumptions and uncertainty.
- `docs/` = description/specification of actual implementation; its scope and verification state must be explicit.
- `experiments/` = experimental runs with configurations, scripts, metrics, provenance and analysis. Do not equate development logs with published evidence.
- `datasets/` = catalog/manifests/download instructions/synthetic fixtures; raw actual radar files excluded from Git unless explicitly approved and licensed.
- `thesis/` = thesis manuscript and figures; not a duplicate repository of research evidence.
- `ai/` = concise state, protocol and handoff information for agents; not an uncontrolled second knowledge base.

## 4. Required implementation outputs (create content, not just folders)

### Repository foundations

- `README.md`: purpose, scope, phase status, architecture overview diagram (Mermaid acceptable), repository navigation, **10-minute quickstart**, setup and verification commands, upstream references, how to contribute and where not to store data.
- `AGENTS.md` (~one readable page): project boundaries, canonical file index, no hallucinated measurements, how to run checks, agent-change rules, academic provenance, no secrets or unapproved push.
- `.gitignore` and `.gitattributes`: ignore Python env/cache, FuseSoC/Vivado generated directories, `.runs`, `.cache`, `.Xil`, simulator artifacts, log/waveform/binary/bitstream/large datasets, local tool installs, secrets, proprietary/license data. Ensure `!` exceptions only when deliberate. Avoid accidentally ignoring source `.sv`, `.v`, `.c`, `.py` or wanted reports.
- `.editorconfig`, a basic `Makefile` with `help`, `doctor`, `check` (and optionally `lint`, `test`, `sim`, `fpga` only if functional or clear prerequisite diagnostics); `scripts/maintenance/validate_workspace.py` or equivalent performing meaningful and runnable checks without FPGA tools.
- Minimal GitHub Actions CI for checks that run without hardware/Vivado. Do not fake passing FPGA verification.
- Environment instructions and `environment/tool-versions.md` (under docs/guides or tools) with **available to user / detected in agent runtime / tested / unknown** distinctions; link to original vendor install docs. **Record user-reported Vivado availability as CONFIRMED BY USER, not VERIFIED BY AGENT.** Detect version (`vivado -version`) if accessible. Do not install, redistribute or embed proprietary EDA software.

### Planning and learning

- `planning/roadmap.md`: Phase 0/1/2/3/4/5 with explicit statuses (planned, active, verified, deferred) and gates.
- `planning/phase1-plan.md`: 6 work packages (WP1 platform research, WP2 architecture learning, WP3 RTL sim/firmware, WP4 FPGA bring-up, WP5 peripherals/debug, WP6 validation/characterization), W1–W8 planned from 2026-10-21 through 2026-12-15, dependencies, per-task deliverables, DoD.
- `planning/weekly/week-01.md`: practical initial checklist; CPU/SoC learning, official documentation, environment doctor, upstream acquisition, initial simulator build; mark progress accurately. Include time estimates as rough planning only, not guaranteed delivery.
- Learning plan and reusable note template (`knowledge/README.md` + at least 2 **starter** notes with genuine useful content, marked sourced/draft): RV32I fetch/decode/execute, MMIO/memory map, recommended chapters of Patterson & Hennessy as pointers, *not copied textbook text*.
- `planning/backlog.md` and `milestones.md` are active, understandable and avoid duplicate conflicting status trackers.

### Research and evidence

- `research/literature/literature-matrix.csv` with useful columns such as paper_id, DOI, authors, year, question, architecture, baseline, workload, hardware, methods, measured_metrics, limitations, relevance, evidence_status, source_url, notes_path.
- `research/literature/references.bib` starter **only with verified records**; if no verified records, include an explanatory README and leave empty instead of inventing citations.
- Template for paper notes: bibliographic identity and source, problem, design choice, experiment controls, baseline, numerical outcomes with units, limitations, what is *not* supported, and relevance to thesis; label abstract-only review as such.
- `research/research-questions.md`: promising future accelerator integration questions explicitly **provisional**, not established gap/novelty; Phase 1's goal remains bringing up Ibex on hardware.
- `docs/decisions/`: ADR-0001 repository design and ADR-0002 Ibex-preferred/not-yet-board-selected, with alternatives and evidence, plus template for FPGA choice.

### Engineering and tests

- Integrate or document acquisition of **upstream lowRISC Ibex Demo System** without silently copying or rewriting it. Prefer pinned git submodule **or** a repeatable checkout script with checked remote URL and immutable commit recorded; choose and justify based on the repository's actual dependency model. Preserve upstream licenses, no unreviewed mass-copy of third-party code.
- Reuse upstream FuseSoC/Verilator/Vivado build flow where supported; wrappers must either delegate correctly or explain precisely which prerequisite, board selection, environment variable, or tool access is missing. **No custom fake Ibex build system.**
- Include a **Vivado-aware, board-gated** development workflow: document command-line/batch use (`vivado -mode batch` where suitable), HDL sources/FuseSoC handoff as supported upstream, constraints, synthesis/implementation, timing/utilization reports and bitstream artifacts. Before FPGA board selection, provide a safe `make vivado-check` (or equivalent) and runbook; do not invent a board `.xdc` file, device part or claim bitstream generation completed. Prefer Tcl/scripts and checked-in configuration over committing `.xpr`-generated output unless there is an explicit reason.
- When Vivado is accessible to the agent, **run environment/version checks** and any tests that do not require a selected board. If accessible only on the user’s machine, provide exact reproducible local commands and a report-import path; mark actual FPGA build and hardware validation as **NOT RUN/BLOCKED** until verified.
- Provide initial tests for the workspace's own small utilities, templates or manifests, not an invented 'Ibex simulation passed'.
- Include one small self-contained synthetic dataset fixture if helpful, with explicit generation script/seed and permissive usage; not real radar measurements. Do not create a misleading 'radar measurement'.
- Prepare `docs/architecture/system-context.md`, `docs/design/phase1-scope.md`, `docs/verification/verification-matrix.md`, `docs/guides/local-setup.md`, `docs/guides/simulation.md`, `docs/guides/fpga-bringup.md`, `docs/guides/vivado-workflow.md`, `docs/guides/debugging.md` with actual references to upstream docs. `vivado-workflow.md` must explain how to check version/path, run batch synthesis/implementation once board selected, extract timing/resource reports, locate logs, and distinguish build success from hardware bring-up. Include TBD/blocked board-dependent sections.
- `docs/verification/verification-matrix.md` should include RTL simulation, firmware execution, timing closure, GPIO in/out, UART tx/rx, timer/interrupt, OpenOCD/GDB, reproducible rebuild, resource report, tagged baseline. Mark **NOT RUN** unless evidenced.

### Dataset strategy

- Create machine-readable template `datasets/manifests/dataset-template.yaml` with: dataset ID/name, version, license/restrictions, URL/DOI, capture device, sample format/dimensions/bit width, sample rate if known, local storage path, checksums, extraction/processing steps, split, contributor, citation, validation state.
- `datasets/catalog.md`: candidate public raw ADC radar datasets for later validation. Link sources rather than importing data. Candidates to assess: Xiangyu Gao's TI 77-GHz raw ADC collection, RADIal raw radar dataset; availability/license must be checked before download.
- Dataset raw files should live in a configurable directory such as `$THESIS_DATA_ROOT` outside the Git tree (or an ignored storage mount), with tracked manifest and processing scripts. DVC is **optional when actual large datasets arrive**; do not activate storage remotes or demand credentials now. Git LFS only for deliberately selected moderate-size assets and after evaluating quotas.

### AI Agent workflows

- Root `AGENTS.md` must direct future agents to read `ai/project-context.md`, `ai/current-state.md`, `ai/next-actions.md`, roadmap, active task, and relevant design docs before changes.
- `ai/current-state.md`: date, verified facts, active phase, completed milestones, blockers, environment/board decisions, source revision and references; avoid speculative self-reported progress.
- `ai/next-actions.md`: max ~5 prioritized, actionable tasks with prerequisites, commands or resources, expected outputs and acceptance criteria.
- Templates/workflows for: new coding task, research-paper review with citations, weekly learning review, experiment planning+result capture, design decision/ADR, and session handoff.
- Session handoff must explicitly report changed files, commands/tests actually run, tests blocked/unrun, important decisions, unresolved questions and next smallest action.
- Do not invent agent personas requiring external plugins. Keep conventions tool-agnostic. Agents propose changes as small reviewable commits/PRs; destructive operations, external publishing and data downloads require explicit approval.

## 5. Version control and execution policy

- Prefer a **private** GitHub repository initially. If GitHub account/repo is not authorized, create local Git repo or downloadable archive and give exact authorized next steps. Never assume an account or push without user review/authorization.
- Work on feature branches/commits with understandable messages when feasible. Include GitHub ISSUE_TEMPLATE (task/bug/experiment/reading) and PR checklist.
- Do not accidentally commit upstream build outputs, Vivado projects generated files (`.Xil`, `.runs`, `.cache`, `.gen`), Vivado license files, downloaded PDFs, sensitive radar data, proprietary company artifacts, entire tool installations, huge Git history or temporary raw data. Check in design source, constraints, reproducible Tcl and compact reports when appropriate.
- Recommend backups for local-only/raw data; **Git is not a data backup system**.
- Preserve original source/provenance, add citation links, never claim research novelty as proven.
- Do not reformat/overwrite existing files if re-running the setup; scripts should be idempotent or clearly warn.
- Use a lockfile/pin when it fits upstream; do not introduce unnecessary environment managers if they conflict with official FuseSoC flow.
- Make each test status explicit: PASS, FAIL, BLOCKED, NOT RUN with supporting log/path. Do not label tool absence as successful testing.

## 6. Phase 1 execution plan (to instantiate in planner)

| Week | Window | Engineering milestone | Learning counterpart |
|---|---|---|---|
| W1 | Oct 21–27 | Ibex/core/board research; workspace setup; first environment checks | ISA RV32I/M/C, core vs SoC, fetch/decode/execute |
| W2 | Oct 28–Nov 3 | Upstream demo build; first C firmware under Verilator | register file, datapath, assembler/linker |
| W3 | Nov 4–10 | trace memory map/peripheral wiring; waveforms | pipeline, hazards, memory interfaces |
| W4 | Nov 11–17 | Use **available Vivado** for board-selected synthesis/implementation/bitstream; run `vivado -version` and setup checks earlier in W1 if agent can access tool | FPGA mapping, timing closure, constraints |
| W5 | Nov 18–24 | GPIO, UART and small CLI firmware | MMIO, bus transactions and peripheral registers |
| W6 | Nov 25–Dec 1 | timer/interrupt and OpenOCD/GDB | interrupts, CSRs, debug |
| W7 | Dec 2–8 | repeated validation, counters, reports | CPI, cycle counting, profiling |
| W8 | Dec 9–15 | tagged, documented reproducible FPGA baseline v1 | architecture synthesis and documentation |

Do not mark W1–W8 done by calendar alone. Use real logs and clear gates. Hardware-dependent activities remain BLOCKED until board/environment available.

## 7. Acceptance criteria (mandatory)

A. The user can navigate `README.md` and find each major function in one or two clicks/links. No serious broken internal links; no empty README marketing sections.

B. From root, `make help`, `make doctor`, and at least one **tool-independent** check actually work. Include observed results. A Vivado-specific diagnostic command (`make vivado-check` or equivalent) exists. **Vivado is available to the user**, but if the agent cannot run it in its execution environment, report **USER-AVAILABLE / AGENT-NOT-VERIFIED**, not “Vivado missing from user system” or a fabricated PASS. Board-dependent build checks remain BLOCKED until board/device is selected.

C. Git repo/file hygiene: meaningful ignore rules verified with representative patterns; no secrets, datasets, toolchains or license files tracked. CI checks the same lightweight validations.

D. Phase 1 has real task IDs/statuses, WP1–WP6, learning modules CA01–CA08, planned milestones, DoD and week-one actionable checklist.

E. `AGENTS.md` and `ai/` state/handoff protocol are concise and actionable; an agent can infer current phase and choose an appropriate next small task without knowing this conversation.

F. Research paper, knowledge note, ADR, test case and experiment templates exist and contain evidence/uncertainty fields. Bibliography must not have invented entries.

G. Dataset plan explicitly excludes raw large files from Git and captures provenance/licensing; no unauthorized downloading/uploading.

H. Upstream Ibex strategy documents pin/revision and licenses; `make sim` is either verified against a real upstream tree and marked PASS, or explicitly BLOCKED/NOT RUN with instructions, **never fake success**. The Vivado flow must similarly distinguish version check, synthesis, implementation, timing closure, bitstream and physical FPGA bring-up as **separate** verification states.

I. A final `WORKSPACE_HANDOFF_REPORT.md` details repository tree, what's actually implemented, tests run with outputs, open issues, assumptions, tool requirements, user actions required, and first 5 next tasks.

J. Produce an accessible **real deliverable**: a local workspace/repository when permission/access supports it, otherwise a downloadable archive ready to clone or initialize. Upload to GitHub only if authorized; suggest private visibility first.

## 8. Suggested task order for GPT Work

1. Inspect current Project materials/files if accessible. Resolve conflicts in writing; no invented facts from inaccessible files.
2. Check current official Ibex Demo System docs and repository dependencies/build conventions. Record confirmed URLs, branch/commit and what was actually verified. **Recognize user-reported Vivado availability** and, when local execution access exists, detect the installed Vivado version early.
3. Implement core skeleton: README, Makefile, AGENTS, docs, planning, knowledge, research, AI context, .gitignore, templates.
4. Implement and run tool-independent checks and the Vivado availability check where possible; supply scripts and simple sample fixtures; optionally acquire pinned upstream if tools/network allow. Do not require a chosen FPGA board to validate the generic workspace.
5. Populate W1 and Phase 1 learning/engineering plan; distinguish active and future phase.
6. Create/verify Git history/CI if allowed; provide final handoff and quickstart commands.
7. Ask user approval before GitHub push, public visibility, secrets, nontrivial downloads, proprietary tool installs, purchases or destructive changes.

## 9. Final response format for the implementing agent

- **Workspace location/download:** exact folder/repo URL or downloadable ZIP.
- **Implemented now:** concise checklist, not promises.
- **Validation evidence:** commands executed and actual PASS/FAIL/BLOCKED.
- **Tool/board assumptions:** distinguish **Vivado available to user** from **Vivado executable tested by agent**; board still TBD, and physical FPGA tests must not be claimed.
- **Repository navigation:** links to README, roadmap, Week 1, AGENTS, current-state and lab runbook.
- **User actions needed:** limited to essential approvals or local-only activities.
- **Next 5 actions:** from `ai/next-actions.md`.

> **Core guardrail:** A smaller operational repository with accurate state, tested setup utilities and excellent navigation is preferable to a beautiful but non-functional empty scaffold. Build Phase 1 first; prepare interfaces for later research without implementing Phase 2–5 prematurely.
