# Bài 3: Tìm chuỗi con trong chuỗi
st = input("Nhập chuỗi: ")
st_search = input("Nhập chuỗi cần tìm: ")
pos = st.find(st_search)
if pos != -1:
    print("Đã tìm thấy tại vị trí:", pos)
else:
    print("Không tìm thấy")
