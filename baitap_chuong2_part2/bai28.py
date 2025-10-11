# Bài 28: Số ngày trong tháng (tháng 2: 28 hoặc 29)
month = input("Nhập tên tháng tiếng Anh (ví dụ: January): ").strip().lower()
days_31 = {"january","march","may","july","august","october","december"}
days_30 = {"april","june","september","november"}
if month in days_31:
    print(31)
elif month in days_30:
    print(30)
elif month == "february":
    print("28 hoặc 29")
else:
    print("Tháng không hợp lệ")
