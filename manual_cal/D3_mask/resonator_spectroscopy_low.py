from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="resonator_spectroscopy_low_4",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    resonator_low = e.resonator_spectroscopy(
        amplitude = 0.03,
        freq_step = 200000,
        freq_width = 60000000,
        power_level = "low",
        #fit_function = "s21",
        relaxation_time = 100000,
    )

report(e.path, e.history)
