# =============================================
# BÀI 4 - Slide 65: Indexing bằng điều kiện boolean
# =============================================
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print("Mảng gốc:\n", a)

# Tạo mảng boolean: True nếu phần tử > 2
bool_idx = a > 2
print("\nMảng boolean (a > 2):\n", bool_idx)

# Lấy tất cả phần tử thỏa điều kiện
print("\nCác phần tử lớn hơn 2:", a[a > 2])