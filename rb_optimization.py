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

from qibocal.auto.execute import Executor
from qibocal import update
from qibocal.auto.operation import Data, Parameters, Results, Routine
from qibocal.config import log
from qibocal.protocols.drag import _acquisition

target = "D1"
platform = "qw11q"
#devo chiamare l'esecutore per far funzionare la routine?
#immagino di non aver bisogno di chiamare l'esecutore però devo controllare di passare correttamente gli argomenti (controllare tipi)
#NB: devo definire una funzione ch prenda come argomento l'esecutore

def test_rb_optimization(executor, _acquisition,
    #drag_output = e.drag_tuning(beta_start=-4, beta_end=4, beta_step=0.5)
         
):
    
    return None

target = "D1"
executor = Executor(
    "myexec",
    path="test_rb",
    platform=platform,
    targets=[target],
    update=True,
    force=True,
) 
  
executor.platform.settings.nshots = 2000

