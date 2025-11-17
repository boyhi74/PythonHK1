import numpy as np  # Import NumPy

# Tạo mảng số nguyên (int) mặc định
x = np.array([1, 2])
print("x =", x)
print("dtype của x =", x.dtype)  # Kiểu dữ liệu int32 hoặc int64 tùy máy

# Tạo mảng số thực (float)
x = np.array([1.0, 2.0])
print("x =", x)
print("dtype của x =", x.dtype)  # Thường là float64

# Tạo mảng số nguyên nhưng ép kiểu rõ ràng là int64
x = np.array([1, 2], dtype=np.int64)
print("x =", x)
print("dtype của x =", x.dtype)  # Bắt buộc là int64
