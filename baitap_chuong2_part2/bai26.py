# Bài 26: Phân loại nguyên âm/phụ âm (tiếng Anh)
ch = input("Nhập một chữ cái: ").strip()
if len(ch) != 1 or not ch.isalpha():
    print("Vui lòng nhập đúng 1 chữ cái.")
else:
    c = ch.lower()
    if c in "aeiou":
        print("Nguyên âm")
    elif c == "y":
        print("Y có thể là nguyên âm hoặc phụ âm")
    else:
        print("Phụ âm")
