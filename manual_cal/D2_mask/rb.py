from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="standard_rb",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 100

    standard_rb = e.standard_rb(
        depths = [1, 5, 10, 20],
        niter = 20,
    )

report(e.path, e.history)
