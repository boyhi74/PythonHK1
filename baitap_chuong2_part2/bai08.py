# Bài 8: Loại bỏ ký tự không phải chữ/số
to_remove = "!()-[]{};:\"\\,<>./?@#$%^&*_~"
my_str = input("Nhập chuỗi: ")
out = ""
for ch in my_str:
    if ch not in to_remove:
        out += ch
print(out)
