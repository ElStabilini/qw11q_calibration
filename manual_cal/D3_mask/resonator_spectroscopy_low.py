from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D3" 
with Executor.open(
    "myexec",
    path="resonator_spectroscopy_low_3",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    resonator_low = e.resonator_spectroscopy(
        amplitude = 0.01,
        freq_step = 100000,
        freq_width = 150000000,
        power_level = "low",
        #fit_function = "s21",
        relaxation_time = 100000,
    )

report(e.path, e.history)
