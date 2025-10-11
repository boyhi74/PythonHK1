# Bài 11: Lưu vào danh sách rồi tính trung bình
nums = []
while True:
    x = input("Nhập số (gõ 'done' để kết thúc): ")
    if x.strip().lower() == "done":
        break
    nums.append(float(x))
print("Giá trị trung bình:", sum(nums)/len(nums) if nums else 0)
print(nums)
