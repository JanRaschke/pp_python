from typing import List

def mat_transpose(mat: List[List[float]]) -> List[List[float]]:  # 1 Punkt
    # Wenn die Matrix leer ist, geben wir eine leere Liste zurück
    if not mat:
        return []
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

print_matrix(mat_transpose(a))