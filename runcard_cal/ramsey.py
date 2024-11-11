from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D1"
with Executor.open(
    "myexec",
    path="recalD1_061124/ramseys_1",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:

    e.platform.settings.nshots = 1024
    ramsey_output = e.ramsey(
        delay_between_pulses_end=1000,
        delay_between_pulses_start=10,
        delay_between_pulses_step=20,
        detuning=3000000,
        relaxation_time=200000,
    )

    if ramsey_output.results.chi2[target][0] < 2:
        ramsey_output.update_platform(e.platform)

    e.platform.settings.nshots = 5000
    classification = e.classification(
        unrolling=False,
    )

report(e.path, e.history)
