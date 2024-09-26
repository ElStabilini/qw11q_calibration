import pathlib
from qibolab import create_platform

from qibocal.auto.execute import Executor
from qibocal.auto.mode import ExecutionMode
from qibocal.protocols import resonator_spectroscopy

# allocate platform
platform = create_platform("....")

#creare executor
executor = Executor.create(
  platform=platform,
  output=pathlib.Path("experiment_data")
)
