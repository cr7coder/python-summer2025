# # # def taoL(n):
# # #     A = []  # chứa số
# # #     B = []  # chứa chuỗi
# # #     C=set()
# # #     for i in range(n):
# # #         dl = input(f"Nhập giá trị thứ {i+1}: ")
# # #         try:
# # #             number=int(dl)
# # #             C.add(number)
# # #         except ValueError:
# # #             try:
# # #                 number = float(dl)  # nếu nhập được số
# # #                 A.append(number)
# # #             except ValueError:
# # #                 B.append(dl)  # nếu không phải số thì thêm vào B
# # #     return A,C, B

# # # n = int(input("N = "))
# # # A,C, B = taoL(n)

# # # print("Tổng các phần tử của A =", sum(A))
# # # print("C=",C)
# # # print("Danh sách B =", "-".join(B))
# # def nhap(n):
# #     A=[]
# #     B=[]
# #     for i in range(n):
# #         dl=input(f"DL - {i+1}: ")
# #         try:
# #             number=float(dl)
# #             A.append(number)
# #         except ValueError:
# #             B.append(dl)
# #     return A,B
# # def main():
# #     n=int(input("N="))
# #     A,B=nhap(n)
# #     print("DS a:")
# #     print(A)
# #     print("DS B:")
# #     print("-".join(B))
# #     print(f"TBC a:",sum(A)/len(A))
# # main()

# def chiahetchoAB(n,a,b):
#     ds=[]
#     for i in range(2,n):
#         if i%a==0 and i%b==0:
#             ds.append(i)
#     return ds
# def chiahetchoAkB(n,a,b):
#     ds=[]
#     for i in range(2,n):
#         if i%a==0 and i%b!=0:
#             ds.append(i)
#     return ds
# def snt(x):
#     if x<2:
#         return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# def SNT(n,a,b):
#     ds=[]
#     for i in range(2,n):
#         if snt(i):
#             ds.append(i)
#     return ds
# def scp(x):
#     return int(x**0.5)**2==x
# def SCP(n,a,b):
#     ds=[]
#     for i in range(2,n):
#         if scp(i) and i%2==0:
#             ds.append(i)
#     return ds

# def main():
#     a=int(input("A="))
#     b=int(input("B="))
#     n=int(input("N="))
#     u=chiahetchoAB(n,a,b)
#     print(u)
#     s=chiahetchoAkB(n,a,b)
#     print(s)
#     y=SCP(n,a,b)
#     print(y)
#     z=SNT(n,a,b)
#     print(z)
# main()
    

a=int(input("A="))
b=int(input("B="))
n=int(input("N="))

def scp(x):
    return int(x**0.5)**2==x
def snt(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
print(f"chia het cho a va b la:",[i for i in range(2,n) if i%a==0 and i %b==0])
print(f"chia het cho a kong chia b la:",[i for i in range(2,n) if i%a==0 and i %b!=0])
print(f"Scp:",[i for i in range(2,n) if scp(i) and i%2==0 ])
print(f"snt:",[i for i in range(2,n) if snt(i)])
