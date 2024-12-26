import pyturb
import pyturb.utils.constants as cts
from pyturb.gas_models.perfect_ideal_gas import PerfectIdealGas
from pyturb.gas_models.perfect_ideal_gas import SemiperfectIdealGas
from pyturb.gas_models.gas_mixture import GasMixture
import numpy as np

air = PerfectIdealGas('Air')
gas_mixture_p_air = GasMixture(gas_model='Perfect')

gas_mixture_p_air.add_gas('O2', 0.209476)

print(vars(air))
print(air._gas_species)
