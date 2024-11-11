from qibocal.auto.execute import Executor
from qibocal.cli.report import report

# this protcol might probably change
target = "D2"
with Executor.open(
    "myexec",
    path="rabi_amplitude",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    rabi = e.rabi_amplitude_signal(
        min_amp_factor=0.0,
        max_amp_factor=2,
        step_amp_factor=0.1,
        relaxation_time=100000,
        pulse_length=40,
    )

report(e.path, e.history)
