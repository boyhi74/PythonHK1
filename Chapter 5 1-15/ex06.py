import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print("Cộng: \n", x + y)
print("Trừ: \n", x - y)
print("Nhân từng phần tử: \n", x * y)
print("Chia: \n", x / y)
print("Căn bậc 2 của x: \n", np.sqrt(x))