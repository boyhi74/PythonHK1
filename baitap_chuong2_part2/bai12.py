# Bài 12: Số chia hết cho 7 nhưng không chia hết cho 5 từ 2000..3200
ans = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        ans.append(str(i))
print(",".join(ans))
