import matplotlib.pyplot as plt
from utils import make_error_rate_figure
from qldpc.codes import SurfaceCode
import numpy as np

# Surface codes using built-in function
surface_codes = [SurfaceCode(dist) for dist in [3, 7, 11, 15]]
surface_code = [SurfaceCode(dist, rotated=True) for dist in [3, 7, 11, 15]]
make_error_rate_figure(surface_code, with_MWPM=True, physical_rates= np.logspace(-3,-0.01,100))
plt.show()