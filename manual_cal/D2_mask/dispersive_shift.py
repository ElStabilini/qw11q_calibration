from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="dispersive_shift",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    dispersive_shift = e.dispersive_shift(
        freq_width = ,
        freq_srep = ,
    )

report(e.path, e.history)
