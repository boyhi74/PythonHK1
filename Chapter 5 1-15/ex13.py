import numpy as np  # Import NumPy

# Ma trận 4x3
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

# Vector 1x3
v = np.array([1, 0, 1])

# Nhờ broadcasting, v sẽ được "dàn" ra cho từng hàng của x
y = x + v

print("x =\n", x)
print("v =", v)
print("y = x + v (broadcasting) =\n", y)
