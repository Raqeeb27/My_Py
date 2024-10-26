from time import sleep

print("\n---- MULTIPLICATION OF MATRICES ----\n")

sleep(0.5)

# Get the matrix dimensions
n = int(input("Enter the dimension of the square matrices (e.g., enter 2 for 2x2 matrix): "))

# Input elements for matrix A and matrix B
a = [int(x) for x in input("Enter elements of Matrix A (row by row): ").split()]
b = [int(x) for x in input("Enter elements of Matrix B (row by row): ").split()]

# Convert flat list into 2D matrices
matrix_a = [a[i * n:(i + 1) * n] for i in range(n)]
matrix_b = [b[i * n:(i + 1) * n] for i in range(n)]

# Matrix Multiplication
matrix_multiplication = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

# Display results
print("\nMatrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nMatrix Multiplication (A * B):")
for row in matrix_multiplication:
    print(row)
