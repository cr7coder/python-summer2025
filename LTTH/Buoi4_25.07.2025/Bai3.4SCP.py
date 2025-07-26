# def ktraSCP(x):
#     return int(x**0.5)**2 == x

# def SCP(n, m):
#     ds = []
#     for i in range(min(n, m) + 1, max(n, m)):
#         if ktraSCP(i):
#             ds.append(i)
#     return tuple(ds) if len(ds)>0 else 0

# try:
#     n = int(input("N = "))
#     m = int(input("M = "))
#     assert n > 0 and m > 0, "n và m phải là số nguyên dương!"
#     kq = SCP(n, m)
#     if kq==0:
#         print("K có scp")  
#     else:
#         print(f"Các số chính phương trong đoạn [{n},{m}] là: {kq}")
# except ValueError:
#     print("Lỗi: Vui lòng nhập số nguyên!")
# except AssertionError as e:
#     print(e)


def ktraSCP(x):
    return int(x**0.5)**2 == x

try:
    n = int(input("N = "))
    m = int(input("M = "))
    assert n > 0 and m > 0, "n và m phải là số nguyên dương!"
    B = tuple(i for i in range(min(n, m) + 1, max(n, m)) if ktraSCP(i))
    print(f"Các số chính phương trong khoảng ({min(n,m)},{max(n,m)}) là:")
    print(B)

except ValueError:
    print("n phải nguyên")
except AssertionError as e:
    print(e)
