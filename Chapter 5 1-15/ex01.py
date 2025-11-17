# =============================================
# BÀI 1 - Slide 62: Tạo mảng NumPy cơ bản, kiểm tra kiểu, shape, truy cập phần tử
# =============================================
import numpy as np

# Tạo mảng 1 chiều từ list
a = np.array([1, 2, 3])
print("Kiểu dữ liệu của a:", type(a))           # <class 'numpy.ndarray'>
print("Kích thước (shape) của a:", a.shape)     # (3,)
print("Các phần tử:", a[0], a[1], a[2])

# Thay đổi giá trị phần tử
a[0] = 5
print("Mảng a sau khi sửa:", a)

# Tạo mảng 2 chiều (ma trận)
b = np.array([[1, 2, 3], [4, 5, 6]])
print("\nShape của ma trận b:", b.shape)        # (2, 3)
print("Phần tử b[0,0] =", b[0, 0])
print("Phần tử b[0,1] =", b[0, 1])
print("Phần tử b[1,0] =", b[1, 0])