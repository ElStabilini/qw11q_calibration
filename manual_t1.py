import pathlib
from qibolab import create_platform

from qibocal.auto.execute import Executor
from qibocal.auto.mode import ExecutionMode
from qibocal.protocols import t1_signal

# allocate platform
platform = create_platform("dummy")

#creare executor
executor = Executor.create(
  platform=platform,
  name='dummy test'
  #output=pathlib.Path("experiment_data")
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
results = t1_res.results  # fit data
