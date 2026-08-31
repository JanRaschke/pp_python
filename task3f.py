import numpy as np
from typing import List, Tuple

def random_array(*shape: int) -> Tuple[List[List[float]], np.ndarray]:  # 1 Punkt
    np_large = np.random.rand(*shape)
    
    mat_large = np_large.tolist()

    return mat_large, np_large

mat_large, np_large = random_array(500, 500)

# 1 Punkt
print("Numpy Transpose:")
%time _ = np_transpose(np_large)
print()

print("List Transpose:")
%time _ = mat_transpose(mat_large)
print()

print("Numpy Addition:")
%time _ = np_add(np_large, np_large)
print()

print("List Addition:")
%time _ = mat_add(mat_large, mat_large)
print()

print("Numpy Multiplication:")
%time _ = mat_mul_imperative(np_large, np_large)
print()

print("List Multiplication:")
%time _ = mat_mul_imperative(mat_large, mat_large)
print()