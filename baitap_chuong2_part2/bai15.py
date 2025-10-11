# Bài 15: Nhập chuỗi số ngăn cách bởi dấu phẩy -> list và tuple
s = input("Nhập các giá trị (phân cách bởi dấu phẩy): ")
items = s.split(",")
print(items)
print(tuple(items))
