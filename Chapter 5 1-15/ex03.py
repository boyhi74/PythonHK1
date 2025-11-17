# BÀI 3 - Slide 64: Slicing mảng

import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Mảng gốc:\n", a)

# Cắt 2 hàng đầu, 2 cột giữa → b là VIEW của a
b = a[:2, 1:3]
print("\nSlice b (2x2):\n", b)

print("\nPhần tử a[0,1] ban đầu =", a[0, 1])   # 2

# Thay đổi b → a cũng thay đổi!
b[0, 0] = 99
print("Sau khi sửa b[0,0] = 99")
print("Mảng a giờ là:\n", a)
print("→ Chứng tỏ slicing tạo VIEW, không phải copy!")