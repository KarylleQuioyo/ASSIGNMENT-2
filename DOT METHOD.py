import numpy as np

# Examples of dot method

# Example 1
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product1 = np.dot(A, B)
print("Dot product of A and B (Example 1):\n", dot_product1)

# Example 2
C = np.array([1, 2])
D = np.array([3, 4])
dot_product2 = np.dot(C, D)
print("Dot product of C and D (Example 2):", dot_product2)

# Example 3
E = np.array([[1, 4, 6], [2, 7, 8], [3, 0, 5]])
F = np.array([[2, 3, 1], [1, 0, 5], [4, 6, 7]])
dot_product3 = np.dot(E, F)
print("Dot product of E and F (Example 3):\n", dot_product3)

