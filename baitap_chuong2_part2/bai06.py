# Bài 6: Đếm ký tự hoa và thường
s = input("Nhập câu: ")
u = 0
l = 0
for ch in s:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1
print("Chữ hoa:", u)
print("Chữ thường:", l)
