# s = input("S: ")
# s = s.split()

# min_len = min(len(x) for x in s)
# s = ["$" if len(x) == min_len else x for x in s]
# kq = " ".join(s)
# print("S: ",kq)

# s=input("s=")
# s=s.split()
# ngan= min(len(x) for x in s )
# u=["!!" if len(x)== ngan else x for x in s]
# kq=" ".join(u)
# print(kq)

# n=input("Day so:")
# n=n.split(",")
# ds=[ int(x) for x in n]
# ds.reverse()
# print(ds)
def phantich(n):
    if n%2!=0:
        return []
    ds=[]
    for a in range(2,n,2):
        for b in range (2,n-a,2):
            for c in range(2,n-a-b,2):
                d=n-a-b-c
                if n>=2 and n%2==0:
                    ds.append(tuple([a,b,c,d]))
    return ds

n=int(input("N="))
a=phantich(n)
print(f"Co {len(a)} cach phân tích {n} thanh 4 số nguyên dương chẵn")
print(a)
