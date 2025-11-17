import numpy as np  # Import NumPy

# Vector v length 3
v = np.array([1, 2, 3])
# Vector w length 2
w = np.array([4, 5])

# np.reshape(v, (3,1)) -> v từ (3,) thành (3,1)
# Nhân với w (shape (2,)) -> broadcasting -> ma trận 3x2
print("np.reshape(v, (3,1)) * w =\n", np.reshape(v, (3, 1)) * w)

# Ma trận 2x3
x = np.array([[1, 2, 3],
              [4, 5, 6]])
print("x =\n", x)

# x + v: v có shape (3,), được broadcast theo cột -> cộng vào từng hàng
print("x + v =\n", x + v)

# x.T có shape (3,2); w có shape (2,)
# x.T + w -> broadcast w theo hàng, rồi .T lại để về 2x3
print("(x.T + w).T =\n", (x.T + w).T)

# np.reshape(w, (2,1)) -> w trở thành (2,1)
# x + reshape(w) -> broadcast theo hàng -> cộng vào từng cột của x
print("x + np.reshape(w, (2,1)) =\n", x + np.reshape(w, (2, 1)))
