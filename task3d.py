import numpy as np 
from typing import List

# 1 Punkt

# Transpose
def np_transpose(mat: List[List[float]]) -> np.ndarray:
    return np.array(mat).T

# Add
def np_add(mat1: List[List[float]], mat2: List[List[float]]) -> np.ndarray:
    return np.array(mat1) + np.array(mat2)

# Multiply
def np_mul(mat1: List[List[float]], mat2: List[List[float]]) -> np.ndarray:
    return np.dot(mat1, mat2)

assert (np_transpose(a) == mat_transpose(a)).all(), "Transpose result is not identical"
assert (np_add(a, b) == mat_add(a,b)).all() , "Addition result is not identical"
assert (np_mul(a,c) == mat_mul_imperative(a,c)).all(), "Multiplication result is not identical"
print("All results are identical")