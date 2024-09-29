'''REPLICATE RESULTS FOR D2 CALIBRATION 

goal of this script is to replicate the results obtained for the D2 calibration for 
high power spectroscopy using the API and qibocal as library instead of using

''' 

from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="manual_resonator_D2",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 1024

    resonator_high = e.resonator_spectroscopy(
        amplitude = 0.05,
        freq_step = 100000,
        freq_width = 20000000,
        power_level = "high",
        relaxation_time = 100000,
    )

report(e.path, e.history)
