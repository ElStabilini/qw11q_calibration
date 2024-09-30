from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="qubit_flux_dependence_1",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    qubit_flux = e.qubit_flux(
        bias_step = 0.002 ,
        bias_width = 0.1,
        drive_amplitude = 0.001,
        drive_duration = 4000,
        freq_step = 50000,
        freq_width = 10000000,
        relaxation_time = 20000,
    )

report(e.path, e.history)
