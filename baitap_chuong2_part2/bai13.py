# Bài 13: Nhập nhiều dòng, in IN HOA
lines = []
print("Nhập từng dòng (để trống để kết thúc):")
while True:
    s = input()
    if s == "":
        break
    lines.append(s.upper())
for line in lines:
    print(line)
