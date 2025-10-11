# Bài 2: Kiểm tra chuỗi hoa/thường/hỗn hợp
st = input("Nhập chuỗi: ")
if st.isupper():
    print("Chuỗi hoa")
elif st.islower():
    print("Chuỗi thường")
else:
    print("Chuỗi chứa cả ký tự hoa và thường")
