def ktraSCP(x):
    return int(x**0.5)**2==x
def ktraSNT(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
n=(input("Day so:"))
n=n.split(",")
ds=[int(x) for x in n]
B = tuple(x for x in ds if ktraSNT(x)) 
print(f"Các số nguyên tố  là:")
print(B)
C=set(x for x in ds if ktraSCP(x))
print(f"Các số Chính phương là:")
print(C)

# def ktraSCP(x):
#     return int(x**0.5)**2==x
# def ktraSNT(x):
#     if x<2:
#         return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# n=input("Day số:")
# n=n.split(",")
# ds=[int(x) for x in n]
# A=[i for i in ds if ktraSCP(i)]
# print("Day so cp la:")
# print(A)
# B=set(i for i in ds if ktraSNT(i))
# print("Day so nt la:")
# print(B)
