# Bài 10: Nhập nhiều số và in giá trị trung bình
total = 0.0
count = 0
while True:
    x = input("Nhập số (gõ 'done' để kết thúc): ")
    if x.strip().lower() == "done":
        break
    total += float(x)
    count += 1
print("Average is:", (total / count) if count else 0)
