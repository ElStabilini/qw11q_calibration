#import pathlib
#from qibolab import create_platform

from qibocal.auto.execute import Executor
from qibocal.cli.report import report
#from qibocal.auto.mode import ExecutionMode
#from qibocal.protocols import t1_signal

target = 0
with Executor.open(
    "myexec",
    path="test_t1_calibration",
    platform="dummy",
    targets=[target],
    update=True,
    force=True, 
) as e:
  e.platform,settings.nshots = 2000

  t1_output = e.t1(
    delay_before_readout_end: 10000
    delay_before_readout_start: 4
    delay_before_readout_step: 100
    nshots: 1000
  ) 

report(e.path, e.history)

"""
allocate platform
platform = create_platform("dummy")
creare executor
executor = Executor.create(
  platform=platform,
  name='dummy test'
  output=pathlib.Path("experiment_data")
)
t1_params = {
    "id": "t1_experiment",
    "targets": [0],  # we are defining here which qubits to analyze
    "operation": "t1_signal",
    "parameters": {
        "delay_before_readout_start": 0,
        "delay_before_readout_end": 20_000,
        "delay_before_readout_step": 50,
    },
}
executor.run_protocol(t1_signal, t1_params, ExecutionMode.ACQUIRE)
executor.run_protocol(t1_signal, t1_params, ExecutionMode.FIT)
history = executor.history
t1_res = history["t1_experiment"]  # id of the protocol
data = t1_res.data  # raw data
results = t1_res.results  # fit data"""
