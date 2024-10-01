from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="flipping",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    flipping = e.flipping(
        nflips_max = ,
        nflips_step = ,
    )

report(e.path, e.history)
