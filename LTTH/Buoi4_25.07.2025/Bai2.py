def PHANTICH(n):
    if n % 2 != 0:
        return []
    ds = []
    for a in range(2, n, 2):
        for b in range(2, n - a, 2):
            for c in range(2, n - a - b, 2):
                d = n - a - b - c
                if d >= 2 and d % 2 == 0:
                    ds.append((a, b, c, d))
    return ds

try:
    n = int(input("N = "))
    assert n > 0, "Không hợp lệ!!"
    d = PHANTICH(n)
    print(f"Có {len(d)} cách phân tích {n} thành tổng 4 số nguyên dương chẵn:")
    print(d)
   
except AssertionError as e:
    print(e)
except ValueError:
    print("N phải là số nguyên")
