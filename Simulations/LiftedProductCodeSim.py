import galois
from qldpc.codes import LPCode
from qldpc.abstract import CyclicGroup, GroupRing, RingMember, RingArray
import matplotlib.pyplot as plt
from utils import make_error_rate_figure
import numpy as np

F2 = galois.GF(2)
C27 = CyclicGroup(27)
C30 = CyclicGroup(30)
C35 = CyclicGroup(35)
C36 = CyclicGroup(36)

ring27 = GroupRing(C27, F2.order)
ring30 = GroupRing(C30, F2.order)
ring35 = GroupRing(C35, F2.order)
ring36 = GroupRing(C36, F2.order)

r27 = C27.generators[0]
r30 = C30.generators[0]
r35 = C35.generators[0]
r36 = C36.generators[0]

# Codes in https://arxiv.org/pdf/2306.16400 Table I (In order: 5, 6, 7, 1, 8, 9th row codes)
a1 = RingMember(ring27, (1, C27.identity), (1, r27**1), (1, r27**3), (1, r27**7))
b1 = RingMember(ring27, (1, C27.identity), (1, r27**1), (1, r27**12), (1, r27**19))
matrix_a1 = RingArray([[a1]])
matrix_b1 = RingArray([[b1]])
code1 = LPCode(matrix_a1, matrix_b1)

a2 = RingMember(ring30, (1, C30.identity), (1, r30**10), (1, r30**6), (1, r30**13))
b2 = RingMember(ring30, (1, C30.identity), (1, r30**25), (1, r30**16), (1, r30**12))
matrix_a2 = RingArray([[a2]])
matrix_b2 = RingArray([[b2]])
code2 = LPCode(matrix_a2, matrix_b2)

a3 = RingMember(ring35, (1, C35.identity), (1, r35**15), (1, r35**16), (1, r35**18))
b3 = RingMember(ring35, (1, C35.identity), (1, r35**1), (1, r35**24), (1, r35**27))
matrix_a3 = RingArray([[a3]])
matrix_b3 = RingArray([[b3]])
code3 = LPCode(matrix_a3, matrix_b3)

a4 = RingMember(ring36, (1, C36.identity), (1, r36**28))
b4 = RingMember(ring36, (1, C36.identity), (1, r36**9), (1, r36**18),
                (1, r36**12), (1, r36**29), (1, r36**14))
matrix_a4 = RingArray([[a4]])
matrix_b4 = RingArray([[b4]])
code4 = LPCode(matrix_a4, matrix_b4)

a5 = RingMember(ring36, (1, C36.identity), (1, r36**9), (1, r36**28), (1, r36**31))
b5 = RingMember(ring36, (1, C36.identity), (1, r36**1), (1, r36**21), (1, r36**34))
matrix_a5 = RingArray([[a5]])
matrix_b5 = RingArray([[b5]])
code5 = LPCode(matrix_a5, matrix_b5)

a6 = RingMember(ring36, (1, C36.identity), (1, r36**9), (1, r36**28), (1, r36**13))
b6 = RingMember(ring36, (1, C36.identity), (1, r36**1), (1, r36**3), (1, r36**22))
matrix_a6 = RingArray([[a6]])
matrix_b6 = RingArray([[b6]])
code6 = LPCode(matrix_a6, matrix_b6)

LPcodes = [code1, code2, code3, code4, code5, code6]

make_error_rate_figure(LPcodes, physical_rates= np.logspace(-3,-0.01,100), num_samples=100, with_BP_OSD=True, distance_estimation_trials=100)
plt.show()