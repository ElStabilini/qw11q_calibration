from qibocal.auto.execute import Executor
from qibocal.cli.report import report

#this protcol might probably change
target = "D2" 
with Executor.open(
    "myexec",
    path="rabi",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    rabi = e.rabi_amplitude_frequency_signal(
        min_amp_factor = ,
        max_amp_factor = ,
        step_amp_factor = ,
        min_freq = ,
        max_freq = ,
        step_freq = ,
        pulse_length = ,
        nshots = , 
    )

report(e.path, e.history)
