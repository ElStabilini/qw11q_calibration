from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="qubit_power_spectroscopy",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    qubit_power_spectroscopy = e.qubit_power_spectroscopy(
        amplitude = ,
        duration = ,
        freq_step = ,
        freq_width = ,
        min_amp_factor = ,
        max_amp_factor = ,
        relaxation_time = ,
        step_amp_factor = ,
    )

report(e.path, e.history)
