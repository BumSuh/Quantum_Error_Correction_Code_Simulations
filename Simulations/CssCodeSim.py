import matplotlib.pyplot as plt
from utils import make_error_rate_figure
from Codes import ShorCode
from qldpc.codes import SteaneCode
import numpy as np


shor_code = ShorCode()      # Shor code built in "Codes"
steane_code = SteaneCode()      # Built-in Steane code
codes = [shor_code, steane_code]

make_error_rate_figure(codes, with_lookup=True, physical_rates=np.logspace(-3, -0.01, 100))
plt.show()
