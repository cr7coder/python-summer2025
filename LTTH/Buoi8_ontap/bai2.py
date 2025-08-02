def PHANTICH(n):
    ds = []
    for a in range(1, n, 2):
        for b in range(1, n - a, 2):
            for c in range(1, n - a - b, 2):
                for d in range(1, n - a - b-c, 2):
                    e = n - a - b - c-d
                    if e >= 1 and e % 2 != 0:
                        ds.append((a, b, c, d,e))
    return ds

try:
    n = int(input("N = "))
    assert n >= 5, "Không hợp lệ!!"
    d = PHANTICH(n)
    print(f"Có {len(d)} cách phân tích {n} thành tổng 5 số nguyên dương lẻ:")
    print(d)
   
except AssertionError as e:
    print(e)
except ValueError:
    print("N phải là số nguyên")
