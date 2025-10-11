# Bài 22: In 5 phần tử đầu và 5 phần tử cuối của list bình phương 1..20
def tao_in_ds():
    ds = []
    for i in range(1, 21):
        ds.append(i**2)
    print(ds[:5] + ds[-5:])

tao_in_ds()
