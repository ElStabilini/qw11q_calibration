from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="T1_T2",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    t2 = e.t2(
        delay_between_pulses_end = ,
        delay_between_pulses_start = , 
        delay_between_pulses_step = ,
        relaxation_time = ,
    )

    t1 = e.t1(
        delay_before_readout_end = ,
        delay_before_readout_start = ,
        delay_before_readout_step = ,
        relaxation_time = ,
    )

report(e.path, e.history)
