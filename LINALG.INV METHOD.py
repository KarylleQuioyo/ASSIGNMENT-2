import numpy as np

# Examples of linalg.inv method

# Example 1
J = np.array([[4, 7, 9], [2, 5, 8], [1, 3, 6]])
J_inv = np.linalg.inv(J)
print("Inverse of J (Example 1):\n", J_inv)

# Example 2
K = np.array([[6, 2, 3], [4, 5, 9], [1, 8, 0]])
K_inv = np.linalg.inv(K)
print("Inverse of K (Example 2):\n", K_inv)

# Example 3
L = np.array([[5, 9], [8, 1]])
L_inv = np.linalg.inv(L)
print("Inverse of L (Example 3):\n", L_inv)