def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.append(list_)
        for j in range(m):
            list_.append(value)
    return matrix
res1 = get_matrix(6, 3 ,4)
res2 = get_matrix(5, 5 ,13)
res3 = get_matrix(4, 4 ,21)
print(res1)
print(res2)
print(res3)