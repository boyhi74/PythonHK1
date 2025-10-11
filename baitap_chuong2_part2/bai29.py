# Bài 29: Phân loại tam giác theo cạnh
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Không tạo thành tam giác")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
else:
    print("Tam giác thường")
