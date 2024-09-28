from qibocal.auto.execute import Executor
from qibocal.cli.report import report

#target = 0
#with Executor.open(
#    "myexec",
#    path="test_rx_calibration",
#    platform="dummy",
#    targets=[target],
#    update=True,
#    force=True,
#) as e:
#    e.platform.settings.nshots = 2000
#
#    rabi_output = e.rabi_amplitude(
#        min_amp_factor=0.5,
#        max_amp_factor=1.5,
#        step_amp_factor=0.01,
#        pulse_length=e.platform.qubits[target].native_gates.RX.duration,
#    )
#
#report(e.path, e.history)