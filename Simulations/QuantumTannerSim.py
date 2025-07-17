import numpy as np
from qldpc.abstract import ProjectiveSpecialLinearGroup
from qldpc.codes import QTCode, RepetitionCode
import matplotlib.pyplot as plt
from utils import make_error_rate_figure

# Quantum Tanner codes built with PSL(2,3), PSL(2,5), and PSL(2,7) groups. PSL groups built using built-in functions.
group1 = ProjectiveSpecialLinearGroup(2, 3)
group2 = ProjectiveSpecialLinearGroup(2, 5)
group3 = ProjectiveSpecialLinearGroup(2, 7)
code_rep = RepetitionCode(3)

qt_code1 = QTCode.random(
    group=group1,
    code_a=code_rep,
)

qt_code2 = QTCode.random(
    group=group2,
    code_a=code_rep,
)

qt_code3 = QTCode.random(
    group=group3,
    code_a=code_rep,
)


codes = [qt_code1, qt_code2, qt_code3]

make_error_rate_figure(codes, physical_rates= np.logspace(-3,-0.01,100), num_samples=100, with_BP_OSD=True, distance_estimation_trials=100)
plt.show()