def transposition_matrix(matrix: list) -> list:
    
    res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[j][i] = matrix[i][j]
    return res

matrix = ((2, 3, 4), (5, 6, 7), (7, 8, 9), (10, 12, 13))
print(f'Matrix: ')
print(*matrix, sep='\n')
print()

tran_matrix = transposition_matrix(matrix)
print(f'Transposition matrix: ')
print(*tran_matrix, sep='\n')