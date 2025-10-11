# Bài 7: Kiểm tra số Armstrong bậc N
num = int(input("Nhập số: "))
bac = int(input("Nhập bậc N: "))
t = num
s = 0
while t > 0:
    d = t % 10
    s += d ** bac
    t //= 10
print(f"{num} là Armstrong bậc {bac}" if s == num else f"{num} không phải Armstrong")
