# Bài 30: Kiểm tra năm nhuận
y = int(input("Nhập năm: "))
is_leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
print("Năm nhuận" if is_leap else "Không phải năm nhuận")
