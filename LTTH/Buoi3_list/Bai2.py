# import math

# def chiahetchoab(n, a, b):
#     ds = []
#     for i in range(1, n + 1):
#         if i % a == 0 and i % b == 0:
#             ds.append(i)
#     return ds

# def chiahetchoAkchiaB(n, a, b):
#     ds = []
#     for i in range(1, n + 1):
#         if i % a == 0 and i % b != 0:
#             ds.append(i)
#     return ds

# def ktraSNT(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def SNT(n):
#     ds = []
#     for i in range(1, n + 1):
#         if ktraSNT(i):
#             ds.append(i)
#     return ds

# def ktraSCP(x):
#    return int(x ** 0.5) ** 2 == x

# def SCPC(n):
#     ds = []
#     for i in range(1, n + 1):
#         if ktraSCP(i) and i % 2 == 0:
#             ds.append(i)
#     return ds

# def main():
    
#     N = int(input("N = "))
#     A = int(input("A = "))
#     B = int(input("B = "))
    
#     ds1 = chiahetchoab(N, A, B)
#     ds2 = chiahetchoAkchiaB(N, A, B)
#     ds3 = SNT(N)
#     ds4 = SCPC(N)

#     print(f'Dãy số chia hết cho  {A} và {B} thuộc [{1},{N}]')
#     print(ds1)
#     print(f'Dãy số chia hết cho {A},không chia hết cho {B} thuộc[{1},{N}]')
#     print(ds2)
#     print(f"Các số nguyên tố từ 1 đến {N}")
#     print(ds3)
#     print(f'Dãy số chính phương chẵn thuộc [{1},{N}]')
#     print(ds4)

# main()
def ktraSCP(x):
    return int(x ** 0.5) ** 2 == x
def SNT(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i==0:
            return False
    return True
def main():
    n = int(input("N = "))
    a = int(input("A = "))
    b = int(input("B = "))

    A=[i for i in range (1,n+1) if i%a==0 and i%b==0]
    B=[i for i in range (1,n+1) if i%a==0 and i%b!=0]
    C=[i for i in range (1,n+1) if ktraSCP(i)and i%2==0]
    D=[i for i in range (1,n+1) if SNT(i)]
   

    

    print(f'Dãy số chia hết cho {a} và {b} thuộc [{1},{n}]:')
    print(A)
    print(f'Dãy số chia hết cho {a}, không chia hết cho {b} thuộc [{1},{n}]:')
    print(B)
    print(f'Dãy số chính phương chẵn thuộc [{1},{n}]:')
    print(C)
    print(f'Dãy số SNT thuộc [{1},{n}]:')
    print(D)
main()
