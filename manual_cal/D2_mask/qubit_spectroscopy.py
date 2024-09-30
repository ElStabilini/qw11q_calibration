from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="qubit_spectroscopy",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    qubit_spectroscopy = e.qubit_spectroscopy(
        drive_amplitude = ,
        drive_duration = ,
        freq_step = ,
        freq_width = ,
        relaxation_time = ,
    )

report(e.path, e.history)
