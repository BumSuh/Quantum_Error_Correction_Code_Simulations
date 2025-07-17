import matplotlib.pyplot as plt
from utils import make_error_rate_figure
from qldpc.codes import ToricCode
import numpy as np

# Toric codes using built-in function
toric_code = [ToricCode(dist, rotated = False) for dist in [3, 7, 11, 15]]
make_error_rate_figure(toric_code, with_MWPM=True, physical_rates= np.logspace(-3,-0.01,100))
plt.show()