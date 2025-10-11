# Bài 4: Số lớn nhất trong 3 số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("Số lớn nhất là:", largest)
