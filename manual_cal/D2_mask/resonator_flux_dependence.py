from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="resonator_flux_dependence_2",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    resonator_flux = e.resonator_flux(
        bias_step = 0.05,
        bias_width = 1,
        freq_step = 100000, 
        freq_width = 10000000,
        drive_amplitude = 0.008,
        relaxation_time = 20000,
    )

report(e.path, e.history)
