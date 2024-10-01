from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="validation",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 5000

    allxy = e.allxy(
        relaxation_time = ,
    )

    state_tomography = e.state_tomography(
        relaxation_time = ,
    )

    readout = e.readout_characterization(
        delay = ,
        relaxation_time = ,
    )

report(e.path, e.history)
