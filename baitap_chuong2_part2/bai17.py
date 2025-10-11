# Bài 17: Đếm chữ cái và chữ số trong chuỗi
s = input("Nhập chuỗi: ")
d = {"chu_cai": 0, "chu_so": 0}
for ch in s:
    if ch.isalpha():
        d["chu_cai"] += 1
    elif ch.isdigit():
        d["chu_so"] += 1
print("Số chữ cái:", d["chu_cai"])
print("Số chữ số:", d["chu_so"])
