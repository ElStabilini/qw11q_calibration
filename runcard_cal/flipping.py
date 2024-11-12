from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D1"
with Executor.open(
    "myexec",
    path="recalD1_061124/flipping_test",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    flipping_output = e.flipping(
        nflips_max=20,
        nflips_step=1,
    )

report(e.path, e.history)

print(flipping_output)

