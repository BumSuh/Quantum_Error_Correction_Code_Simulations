import numpy as np
from qldpc import codes
from qldpc.codes.common import CSSCode


class ShorCode(CSSCode):
    """
    The [9, 1, 3] Shor code created from CSSCode in qldpc/codes/common. The X-parity check matrix
    defined by a kronecker product of I_3 and the 3-bit repetition code. The Z-parity check
    matrix defined by the reverse kronecker product (3-bit repetition code and I_3). Logical
    X is defined with [1, 0, 0, 1, 0, 0, 1, 0, 0] and logical Z is defined with [1, 1, 1, 1,
    1, 1, 1, 1, 1].
    """
    def __init__(self):
        code = codes.RepetitionCode(3)  # 3 qubit repetition code
        self.Hx = np.kron(np.eye(3, dtype=int), code.matrix)
        self.Hz = np.kron(code.matrix, np.eye(3, dtype=int))

        CSSCode.__init__(self, self.Hx, self.Hz, is_subsystem_code=False)
        self.set_logical_ops_xz([[1, 0, 0, 1, 0, 0, 1, 0, 0]], [[1] * 9], validate=False)
        self._dimension = 1
        self._distance_x = self._distance_z = 3