# Bài 27: Tên hình theo số cạnh (3..10)
n = int(input("Nhập số cạnh (3..10): "))
names = {
    3: "Tam giác",
    4: "Tứ giác",
    5: "Ngũ giác",
    6: "Lục giác",
    7: "Thất giác",
    8: "Bát giác",
    9: "Cửu giác",
    10: "Thập giác"
}
print(names.get(n, "Số cạnh ngoài phạm vi hỗ trợ"))
