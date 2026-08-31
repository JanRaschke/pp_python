from typing import List

def mat_add(mat1: List[List[float]], mat2: List[List[float]]) -> List[List[float]]:  # 1 Punkt
    assert len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]), "Shapes do not match"  
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

b = [[10, 20, 30, 40], [50, 60, 70, 80]]

print_matrix(mat_add(a, b))