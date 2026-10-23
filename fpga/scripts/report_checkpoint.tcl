# Workspace utility; no synthesis or programming. NOT yet run in Vivado.
# Usage: vivado -mode batch -source fpga/scripts/report_checkpoint.tcl \
#   -tclargs /absolute/path/to/routed.dcp build/vivado-reports/run-id
if {$argc != 2} {
    puts stderr "Usage: report_checkpoint.tcl <routed.dcp> <output-directory>"
    exit 2
}
set thesis_checkpoint [file normalize [lindex $argv 0]]
set thesis_report_dir [file normalize [lindex $argv 1]]
if {![file isfile $thesis_checkpoint]} {
    puts stderr "Checkpoint does not exist: $thesis_checkpoint"
    exit 2
}
# Require a fresh output directory so an old successful report cannot survive
# alongside a failed new run, and prior evidence is not overwritten.
if {[file exists $thesis_report_dir]} {
    puts stderr "Output directory exists; choose a new run directory: $thesis_report_dir"
    exit 2
}
file mkdir $thesis_report_dir
open_checkpoint $thesis_checkpoint
report_timing_summary -file [file join $thesis_report_dir timing-summary.rpt]
report_utilization -file [file join $thesis_report_dir utilization.rpt]
report_drc -file [file join $thesis_report_dir drc.rpt]
report_route_status -file [file join $thesis_report_dir route-status.rpt]
close_design
puts "Reports written. Review routing, constraints, timing and DRC before assigning a result."
exit 0
