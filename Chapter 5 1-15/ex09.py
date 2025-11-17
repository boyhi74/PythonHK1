import numpy as np  # Import NumPy

# Tạo 2 mảng 2x2 kiểu float64
x = np.array([[1, 2],
              [3, 4]], dtype=np.float64)
y = np.array([[5, 6],
              [7, 8]], dtype=np.float64)

print("x =\n", x)
print("y =\n", y)

# Cộng từng phần tử (element-wise)
print("x + y =\n", x + y)
print("np.add(x, y) =\n", np.add(x, y))

# Trừ từng phần tử
print("x - y =\n", x - y)
print("np.subtract(x, y) =\n", np.subtract(x, y))

# Nhân từng phần tử
print("x * y =\n", x * y)
print("np.multiply(x, y) =\n", np.multiply(x, y))

# Chia từng phần tử
print("x / y =\n", x / y)
print("np.divide(x, y) =\n", np.divide(x, y))

# Căn bậc hai từng phần tử trong x
print("np.sqrt(x) =\n", np.sqrt(x))
