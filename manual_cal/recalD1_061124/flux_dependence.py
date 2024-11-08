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
    
    resonator_flux = e.resonator_flux(
        bias_step = 0.05,
        bias_width = 0.5,
        freq_step = 100000, 
        freq_width = 10000000,
        relaxation_time = 20000,
    )

    qubit_flux = e.qubit_flux(
        bias_step = 0.001 ,
        bias_width = 0.06,
        drive_amplitude = 0.002,
        drive_duration = 4000,
        freq_step = 200000,
        freq_width = 6000000,
        relaxation_time = 20000,
    )