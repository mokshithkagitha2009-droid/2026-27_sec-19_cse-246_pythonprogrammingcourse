a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print("Matrix A:")
for row in a:
    print(row)

print("Matrix B:")
for row in b:
    print(row)

# Matrix Addition
add = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        add[i][j] = a[i][j] + b[i][j]

print("Addition:")
for row in add:
    print(row)

# Matrix Subtraction
sub = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        sub[i][j] = a[i][j] - b[i][j]

print("Subtraction:")
for row in sub:
    print(row)
