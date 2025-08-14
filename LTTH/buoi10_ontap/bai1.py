# n=int(input("Day so: "))
# # tong=0
# # while n:
# #     tong+=n%10
# #     n//=10
# print("Tong:",sum(int(x) for x in str(n)))
def tong(n):
    tong=0
    while n>0:
        # sodu=n%10
        # tong=tong+sodu
        # n=n//10
        sodu=n%10
        tong=tong+sodu
        n=n//10
    return tong
n=int(input("N="))
a=tong(n)
print(f'Tong =',a)