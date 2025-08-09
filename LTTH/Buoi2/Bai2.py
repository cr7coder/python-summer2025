def tong_chan_am(n, m):
    s = 0
    for i in range(min(n,m),max(n,m)+1):
        if i < 0 and i % 2 == 0:
            s += i
    return s

# def la_chinh_phuong(x):
#     return x >= 0 and int(x ** 0.5) ** 2 == x

# def tbc_chinh_phuong(n, m):
#     s = 0
#     dem = 0
#     if n <= m:
#         for i in range(n, m + 1):
#             if la_chinh_phuong(i) and  i % 2 == 0:
#                 s += i
#                 dem += 1
#     else:
#         for i in range(n, m - 1, -1):
#             if la_chinh_phuong(i) and i % 2 == 0:
#                 s += i
#                 dem += 1
#     return s / dem if dem > 0 else 0

def ktraSCP(x):
    return x>=0 and int(x**0.5)**2 == x
def tbcSCP(n,m):
    s=0
    d=0
    for i in range(min(n,m),max(n,m)+1):
        if ktraSCP(i) and i%2==0:
            s+=i
            d+=1
        tbc=s/d if d>0 else 0
    return d,tbc
def ktraSHH(n):
    if n<=0:
        return False
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
    return tong==n
def tongSHH(n,m):
    s=0
    for i in range(min(n,m),max(n,m)+1):
        if ktraSHH(i):
            s+=i
    return s

    
    # if n <= 0:-
    #     return False
    # tong = 0
    # for i in range(1, n):
    #     if n % i == 0:
    #         tong += i
    # return tong == n
# def tongSHH(n, m):
#     s = 0
#     for i in range(min(n, m), max(n, m)+1):
#         if ktraSHH(i):
#             s += i
#     return s 




def tbc_trong_khoang(n, m):
    s = 0
    dem = 0
    for i in range(min(n,m)+1,max(n,m)):
        s += i
        dem += 1
   
    return s / dem if dem > 0 else 0

def main():
    try:
        n = int(input("Nhập n: "))
        m = int(input("Nhập m: "))
        print("1. Tổng các số chẵn âm:", tong_chan_am(n, m))
        sl,tbc=tbcSCP(n,m)
        if sl==0:
            print("k có số chính phương")
        else:
            print("sl scp la:",sl)
            print("2. TBC các số chính phương:", tbc)
        print("3. TBC các số trong khoảng:", tbc_trong_khoang(n, m))
        if tongSHH(n,m)==0:
            print("K có shh")
        else:
            print(f"4.Tổng các số hoàn hảo trong khoảng ({n},{m}) là: ",tongSHH(n,m))

    except ValueError:
        print("Dữ liệu không hợp lệ!")

main()
