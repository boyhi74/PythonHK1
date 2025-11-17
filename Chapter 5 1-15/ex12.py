import numpy as np  # Import NumPy

# Ma trận 4x3
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

# Vector 1x3
v = np.array([1, 0, 1])

# Tạo mảng y có cùng shape với x, chưa có giá trị rõ ràng
y = np.empty_like(x)

# Dùng vòng lặp: với mỗi dòng i của x,
# cộng vector v rồi gán vào dòng i của y
for i in range(4):
    y[i, :] = x[i, :] + v

print("x =\n", x)
print("v =", v)
print("y (sau khi cộng từng dòng với v) =\n", y)
