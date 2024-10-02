from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="ramsey",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    ramsey = e.ramsey(
        delay_between_pulses_end = ,
        delay_between_pulses_start = ,
        delay_between_pulses_step = ,
        detuning = ,
        relaxation_time = ,
    )

report(e.path, e.history)
