# Bài 9: Tách từ và sắp xếp theo alphabet
s = input("Nhập chuỗi: ")
words = s.split()
words.sort()
print("Các từ đã sắp xếp:")
for w_ in words:
    print(w_)
