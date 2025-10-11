# Bài 16: Tạo dict {i: i*i} với i=1..n
n = int(input("Nhập n: "))
d = {}
for i in range(1, n+1):
    d[i] = i*i
print(d)
