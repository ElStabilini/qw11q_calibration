from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D3"
with Executor.open(
    "myexec",
    path="qubit_spectroscopy_2",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    qubit_spectroscopy = e.qubit_spectroscopy(
        drive_amplitude=0.04,
        drive_duration=4000,
        freq_step=50000,
        freq_width=10000000,
        relaxation_time=5000,
    )

report(e.path, e.history)
