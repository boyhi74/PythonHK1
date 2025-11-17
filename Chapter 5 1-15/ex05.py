import numpy as np

x1 = np.array([1, 2])          # NumPy tự chọn kiểu
print("x1 tự động:", x1.dtype) # int32 hoặc int64

x2 = np.array([1.0, 2.0])
print("x2 có số thực:", x2.dtype)  # float64

# Chỉ định kiểu rõ ràng
x3 = np.array([1, 2], dtype=np.float64)
print("Chỉ định float64:", x3.dtype)
print(x3)