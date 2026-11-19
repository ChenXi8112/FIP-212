"""10A02-NumPy初探"""

import numpy as np

n = int(input())
matrix = np.array([float(x) for x in input().split()])
print(*matrix.shape)
print(matrix.ndim)
print(f'{np.linalg.norm(matrix):.3f}')
