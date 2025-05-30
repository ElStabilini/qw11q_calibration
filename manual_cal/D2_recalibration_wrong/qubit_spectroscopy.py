from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2"
with Executor.open(
    "myexec",
    path="qubit_spectroscopy_3",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    qubit_spectroscopy = e.qubit_spectroscopy(
        drive_amplitude=0.1,
        drive_duration=4000,
        freq_step=20000,
        freq_width=4000000,
        relaxation_time=5000,
    )

report(e.path, e.history)
