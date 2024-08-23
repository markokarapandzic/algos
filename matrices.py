def matrix_multiply_recursive(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2):
		raise ValueError("Matrices cannot be multiplied. Invalid dimensions.")

	result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

	def recursive_multiply(i, j, k):
		if k == len(matrix2):
			return

		result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

		recursive_multiply(i, j, k + 1)

	def multiply_row(i, j):
		if i == len(matrix1):
			return

		recursive_multiply(i, j, 0)

		multiply_row(i + 1, j)

	def multiply_column(j):
		if j == len(matrix2[0]):
			return

		multiply_row(0, j)

		multiply_column(j + 1)

	multiply_column(0)

	return result_matrix

# Example matrices
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Multiply matrices recursively
result_recursive = matrix_multiply_recursive(matrix_A, matrix_B)

# Print result
if result_recursive:
    print("Resultant Matrix (Recursive):")
    for row in result_recursive:
        print(row)


def matrix_add_recursive(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2):
		raise ValueError("Matrices cannot be added. Invalid dimensions.")

	result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

	def add_row(i, j):
		if j == len(matrix_B[0]):
			return
	
		result_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]

		add_row(i, j + 1)

	def add_column(i):
		if i == len(matrix_B[0]):
			return

		add_row(i, 0)
		add_column(i + 1)

	add_column(0)

	return result_matrix

result_recursive = matrix_add_recursive(matrix_A, matrix_B)

# Print result
if result_recursive:
    print("Resultant Matrix (Recursive):")
    for row in result_recursive:
        print(row)