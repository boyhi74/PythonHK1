# Bài 19: Top 10 từ xuất hiện nhiều nhất trong file (romeo.txt)
# Lưu ý: cần có file romeo.txt cùng thư mục khi chạy
path = "romeo.txt"
d = {}
try:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for w in line.split():
                d[w] = d.get(w, 0) + 1
    items = []
    for k, v in d.items():
        items.append((v, k))
    items.sort(reverse=True)
    for v, k in items[:10]:
        print(k, v)
except FileNotFoundError:
    print("Không tìm thấy file romeo.txt")
