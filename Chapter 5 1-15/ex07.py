# =============================================
# BÀI 7 - Slide 68: Nhân ma trận và nội tích (dot)
# =============================================
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

print("Nội tích v·w =", np.dot(v, w))
print("x × v =\n", np.dot(x, v))
print("x × y =\n", np.dot(x, y))