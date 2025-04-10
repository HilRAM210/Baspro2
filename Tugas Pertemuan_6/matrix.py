A = [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1]]

B = [[2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2]]

C = []

for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        product = 0
        for k in range(len(B)):
            product += A[i][k] * B[k][j]
        row.append(product)
    C.append(row)

print("Hasil:")
for row in C:
    print(row)
