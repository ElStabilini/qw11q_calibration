'''IDEA: costruire un ciclo di ottimizzazione della RB al variare dei
parametri dell'impulso di DRAG'''

from dataclasses import dataclass, field
from typing import Optional
import json

import numpy as np
import numpy.typing as npt
import plotly.graph_objects as go
from qibolab import AcquisitionType, AveragingMode, ExecutionParameters
from qibolab.platform import Platform
from qibolab.pulses import PulseSequence
from qibolab.qubits import QubitId
from scipy.optimize import curve_fit

from qibocal import update
from qibocal.auto.operation import Data, Parameters, Results, Routine
from qibocal.config import log
from qibocal.protocols.drag import _fit

'''from qibocal.auto.execute import Executor
from qibocal.cli.report import report
from scipy.optimize import least_squares #semplicemente come prova

target = "D1"
with Executor.open(
    "myexec",
    path="test_rx_calibration",
    platform="qw11q",
    targets=[target],
    update=True,
    force=True,
) as e:
    e.platform.settings.nshots = 2000

    drag_output = e.drag_tuning(beta_start=-4, beta_end=4, beta_step=0.5)'''
