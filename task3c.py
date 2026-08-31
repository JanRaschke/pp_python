# 2d matrix
a = [ [1,2,3,4], [5,6,7,8] ]
b = [[10, 20, 30, 40], [50, 60, 70, 80]]
c = [[1, 2], [1, 3], [1, 4], [1, 5]]

# helper function to print a 2d matrix
def print_matrix(mat: List[List[float]]) -> None:
    for row in mat:
        print(row)


def mat_mul_imperative(mat1: List[List[float]], mat2: List[List[float]]) -> List[List[float]]:
    assert len(mat1[0]) == len(mat2), "Shapes do not match"
    
    n = len(mat1)       
    m = len(mat2)       
    o = len(mat2[0])    
    
    result = [[0.0 for _ in range(o)] for _ in range(n)]
    
    for i in range(n):
        for j in range(o):
            for k in range(m):
            
                result[i][j] += mat1[i][k] * mat2[k][j]
                
    return result

print(mat_mul_imperative(a,c))