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
    
    e.platform.settings.nshots = 1024

    qubit_spectroscopy = e.qubit_spectroscopy(
        drive_amplitude = 0.01,
        drive_duration = 4000,
        freq_step = 100000,
        freq_width = 100000000,
        relaxation_time = 5000,
    )

    qubit_power_spectroscopy = e.qubit_power_spectroscopy(
        amplitude = 0.01 ,
        duration = 4000,
        freq_step = 100000,
        freq_width = 300000000,
        min_amp_factor = 0.1,
        max_amp_factor = 2,
        relaxation_time = 5000,
        step_amp_factor = 0.1,
    )