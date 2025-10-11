# Bài 5: Tính S = 1/2 + 2/3 + ... + n/(n+1)
n = int(input("Nhập n (>0): "))
s = 0.0
for i in range(1, n+1):
    s += i/(i+1)
print("Tổng =", s)
