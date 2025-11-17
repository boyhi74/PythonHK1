import numpy as np  # Import NumPy

x = np.array([[1, 2],
              [3, 4]])

print("x =\n", x)

# Tổng tất cả phần tử
print("np.sum(x) =", np.sum(x))

# Tổng theo cột (axis=0) -> [1+3, 2+4]
print("np.sum(x, axis=0) =", np.sum(x, axis=0))

# Tổng theo hàng (axis=1) -> [1+2, 3+4]
print("np.sum(x, axis=1) =", np.sum(x, axis=1))

# Tạo lại x để minh hoạ transpose
x = np.array([[1, 2],
              [3, 4]])

print("x =\n", x)
# Ma trận chuyển vị: đổi hàng thành cột, cột thành hàng
print("x.T =\n", x.T)

# Vector 1D
v = np.array([1, 2, 3])
print("v =", v)
# Với 1D, v.T giống hệt v (chỉ khác nếu dùng mảng 2D dạng cột)
print("v.T =", v.T)
