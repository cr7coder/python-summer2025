# # def la_so(x):
# #     try:
# #         if '.' in x:
# #             return float(x)
# #         else:
# #             return int(x)
# #     except:
# #         return None

# # def main():
# #     A = []
# #     B = []

# #     n = int(input("N = "))
# #     while n<=0:  
# #         n = int(input("N = "))
# #     for i in range(n):
# #         s = input(f"DL - {i+1}: ")
# #         so = la_so(s)
# #         if so is not None:
# #             A.append(so)
# #         else:
# #             B.append(s)
    
# #     print(f"A = {A}")
    
# #     if len(A) > 0:
# #         tbc = sum(A) / len(A)
# #         print(f"TBC: {tbc}")
# #     else:
# #         print("Danh sách A không có phần tử nào.")
    
# #     print(f"B ={B}")
    
# #     if len(B) > 0:
# #         print("Kq:")
# #         print( "-".join(B))
# #     else:
# #         print("Danh sách B không có phần tử nào.")


# # main()
# def createList(n):
#     A=[]
#     B=[]
#     for i in range(n):
#         dl = input(f"DL - {i+1}: ")
#         try:
#             number = float(dl)
#             A.append(number)
#         except ValueError:
#             B.append(dl)
#     return A,B
# def main():
#     while True:
#         n=int(input("N = "))
#         if n>0:
#             break
# # nhập dữ liệu và đưa vào các list
#     A,B= createList(n)
# #in ket qua
#     print("A = ",A)
#     print("TBC:",round(sum(A)/len(A),2))
#     print("B = ",B)
#     print("Kq:")
#     print( "-".join(B))
# main()

def createList(n):
    A=[]
    B=[]
    for i in range (n):
        dl=input(f"DL-{i+1} =")
        try:
            if '.' in dl:
                number=float(dl)
                A.append(number)
            else:
                number=int(dl)
                B.append(number)
        except ValueError:
            print("đưqdưqd")
    return A,B
def main():
    while True:
        n=int(input("N="))
        if n>0:
            break
    A,B=createList(n)
    print(A)
    print(f"TBC:",round(sum(A)/len(A),2))
    print(B)
    print(f"TBC:",round(sum(B)/len(B),2))
main()