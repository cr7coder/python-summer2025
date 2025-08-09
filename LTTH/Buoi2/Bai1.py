# import math

# # def ktraSCP(n):
# #      return int(n ** 0.5) ** 2 == n

# # def demSCP(n, m):
# #     d = 0
# #     for i in range(n, m + 1):
# #         if ktraSCP(i):
# #             d += 1
# #     return d
# def ktraSCP(x):
#         return int(x ** 0.5) ** 2==x #lấy phần nguyên của căn bậc 2 sau đó ktra cb2 mũ 2 == n =>scp
# def demSCP(n,m):
#     d=0
#     for i in range(n,m+1):
#         if ktraSCP(i):
#             d+=1
#     return d
# def ktraSNT(x):
#     if x<2:
#         return False
#     for i in range (2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# def demSNT(n,m):
#     d=0
#     for i in range(n+1,m):
#         if ktraSNT(i):
#             d+=1
#     return d

# # def ktraSNT(x):
# #     if x<2:
# #         return False
# #     for i in range(2,int(x ** 0.5)+1): # duyệt từ 2 đến căn x để ktra ước
# #         if x % i==0: # nếu chia hết số nào trong đoạn đó thì k phải là snt
# #             return False #trả về sai
# #     return True
# # def demSNT(n,m):
# #     d=0
# #     for i in range(n+1,m):
# #         if ktraSNT(i):
# #             d+=1
# #     return d
    
# def ktra_khong_chia_5_6(x):
#     return x % 5 != 0 and x % 6 != 0

# def dem_khong_chia_het_5_6(n):
#     d = 0
#     for i in range(2, n):
#         if ktra_khong_chia_5_6(i):
#             d += 1
#     return d

# def ktra_uoc_20_khong_25(x):
#     return 20 % x == 0 and 25 % x != 0

# def dem_uoc_20_khong_25(n):
#     d = 0
#     for i in range(1, n + 1):
#         if ktra_uoc_20_khong_25(i):
#             d += 1
#     return d

# def Main():
#     try:
#         m = int(input("M="))
#         n = int(input("N="))
#         assert n > 0 and m > 0, "n, m phải là số nguyên dương!"
    
#         d1 = demSCP(m, n)
#         if d1 > 0:
#             print(f"So CP trong [{m},{n}]: {d1}")
#         else:
#             print(f"Khong co so CP nao trong [{m},{n}]")

#         d2 = demSNT(m, n)
#         if d2 > 0:
#             print(f"So SNT trong ({m},{n}): {d2}")
#         else:
#             print(f"Khong co SNT nao trong ({m},{n})")

#         d3 = dem_khong_chia_het_5_6(n)
#         print(f"So trong (1,{n}) khong chia het cho 5 va 6: {d3}")

#         d4 = dem_uoc_20_khong_25(n)
#         print(f"So trong (1,{n}) la uoc cua 20 nhung khong la uoc cua 25: {d4}")

#     except AssertionError as error:
#         print(error)
#     except ValueError:
#         print("Không đúng định dạng!")

# Main()

def KTRASCP(x):
    return int(x**0.5)**2==x
def DEMSCP(n,m):
    d=0
    for i in range(min(n,m),max(n,m)+1):
        if KTRASCP(i):
            d+=1
    return d
def KTRASNT(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def DEMSNT(n,m):
    d=0
    for i in range(min(n,m)+1,max(n,m)):
        if KTRASNT(i):
            d+=1
    return d
def KTRASHH(n):
    if n<0:
        return False
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
    return tong==n
def DEMSHH(n,m):
    d=0
    for i in range(min(n,m)+1,max(n,m)):
        if KTRASHH(i):
            d+=1
    return d
def KTRAFIBO(n):
    return KTRASCP(5*n*n+4) or KTRASCP(5*n*n-4)
def DEMFIBO(n,m):
    d=0
    for i in range(min(n,m)+1,max(n,m)):
        if KTRAFIBO(i):
            d+=1
    return d
def KTRA_ARMSTRONG(n):
    # s = str(n)
    # mu = len(s)
    # tong = sum(int(ch)**mu for ch in s)
    # return tong == n
    s=str(n)
    mu=len(s)
    tong=sum(int(ch)**mu for ch in s)
    return tong==n
def KTRA_DOIXUNG(n):
    # s = str(n)
    # return s == s[::-1]
    s=str(n)
    return s == s[::-1]

def Main():
    n=int(input("N = "))
    m=int(input("M = "))
    print(f'lượng scp trong đoạn [{min(n,m)},{max(n,m)}]la: {DEMSCP(n,m)} ')
    print(f'lượng snt trong đoạn [{min(n,m)},{max(n,m)}]la: {DEMSNT(n,m)} ')
    print(f'lượng shh trong đoạn [{min(n,m)},{max(n,m)}]la: {DEMSHH(n,m)} ')
    print(f'lượng fibo trong đoạn [{min(n,m)},{max(n,m)}]la: {DEMFIBO(n,m)} ')
Main()
