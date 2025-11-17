import numpy as np  # Import NumPy

# Ma trận 2x2
x = np.array([[1, 2],
              [3, 4]])
# Ma trận 2x2 khác
y = np.array([[5, 6],
              [7, 8]])

# Vector 1D độ dài 2
v = np.array([9, 10])
w = np.array([11, 12])

# Tích vô hướng giữa v và w: 9*11 + 10*12
print("v.dot(w) =", v.dot(w))
print("np.dot(v, w) =", np.dot(v, w))

# Nhân ma trận x với vector v -> kết quả 1D
print("x.dot(v) =", x.dot(v))
print("np.dot(x, v) =", np.dot(x, v))

# Nhân ma trận x với ma trận y -> ma trận 2x2
print("x.dot(y) =\n", x.dot(y))
print("np.dot(x, y) =\n", np.dot(x, y))
