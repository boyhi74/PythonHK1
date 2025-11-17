import numpy as np  # Import NumPy

# Vector v length 3
v = np.array([1, 2, 3])
# Vector w length 2
w = np.array([4, 5])

# Outer product bằng reshape + broadcasting
print("np.reshape(v, (3,1)) * w =\n", np.reshape(v, (3, 1)) * w)

# Ma trận 2x3
x = np.array([[1, 2, 3],
              [4, 5, 6]])
print("x =\n", x)

# Cộng v vào từng hàng
print("x + v =\n", x + v)

# Cộng w vào từng cột thông qua chuyển vị
print("(x.T + w).T =\n", (x.T + w).T)

# Cộng w dạng cột vào x
print("x + np.reshape(w, (2,1)) =\n", x + np.reshape(w, (2, 1)))

# Nhân toàn bộ ma trận x với 2 (mỗi phần tử * 2)
print("x * 2 =\n", x * 2)
