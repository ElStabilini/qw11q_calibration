from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D1" 
with Executor.open(
    "myexec",
    path="qubit_calibration",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    
    
    for x in range(3):
        e.platform.settings.nshots = 1024

        ramsey_output = e.ramsey(
            delay_between_pulses_end = 1000,
            delay_between_pulses_start = 10,
            delay_between_pulses_step = 20,
            detuning = 3000000,
            relaxation_time = 200000,
        )

        if ramsey_output.results.chi2[target][0] > 2:
            raise RuntimeError(
                f"Ramsey fit has chi2 {ramsey_output.results.chi2[target][0]} greater than 2. Stopping."
            )

        else:
            ramsey_output.update_platform(e.platform)

        e.platform.settings.nshots = 5000

        classification = e.classification(
        )

report(e.path, e.history)