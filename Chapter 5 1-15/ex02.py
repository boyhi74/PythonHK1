# BÀI 2 - Slide 63: Các hàm tạo mảng đặc biệt
import numpy as np

print("1. Ma trận toàn số 0 (2x2):")
print(np.zeros((2, 2)))

print("\n2. Ma trận toàn số 1 (1x2):")
print(np.ones((1, 2)))

print("\n3. Ma trận toàn số 7 (2x2):")
print(np.full((2, 2), 7))

print("\n4. Ma trận đơn vị 3x3:")
print(np.eye(3))

print("\n5. Ma trận ngẫu nhiên 2x2 (0 đến 1):")
print(np.random.random((2, 2)))