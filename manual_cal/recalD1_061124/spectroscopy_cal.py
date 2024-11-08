from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D1" 
with Executor.open(
    "myexec",
    path="spectroscopy_calibration_2",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    resonator_high = e.resonator_spectroscopy(
        amplitude = 0.2,
        freq_step = 100000,
        freq_width = 10000000,
        power_level = "high",
        relaxation_time = 100000,
    )
    
    resonator_punchout = e.resonator_punchout(
        amplitude = 0.05,
        freq_step = 100000,
        freq_width = 5000000,
        max_amp_factor = 1,
        min_amp_factor = 0.05,
        relaxation_time = 5000,
        step_amp_factor = 0.01,   
    )    

    resonator_punchout.update_platform(e.platform)

    resonator_low = e.resonator_spectroscopy(
        amplitude = 0.01,
        freq_step = 50000,
        freq_width = 20000000,
        power_level = "low",
        fit_function = "s21",
        relaxation_time = 100000,
    )

report(e.path, e.history)
