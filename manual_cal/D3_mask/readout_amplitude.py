from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="readout_amplitude",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    readout_amplitude = e.resonator_amplitude(
        amplitude_step = ,
        amplitude_start = ,
        amplitude_stop = ,
    )

report(e.path, e.history)
