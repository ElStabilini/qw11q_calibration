from qibocal.auto.execute import Executor
from qibocal.cli.report import report

target = "D2" 
with Executor.open(
    "myexec",
    path="resonator_punchout_9",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 2048

    resonator_punchout = e.resonator_punchout(
        amplitude = 0.01,
        freq_step = 2000000,
        freq_width = 400000000,
        max_amp_factor = 2,
        min_amp_factor = 0.1,
        relaxation_time = 5000,
        step_amp_factor = 0.01,    
)

report(e.path, e.history)
