from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2"
with Executor.open(
    "myexec",
    path="classification",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 5000

    classification = e.classification()

report(e.path, e.history)
