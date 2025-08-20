def nhap(i):
    ds=[]
    i=0
    while True:
        masv=input(f"Msv-{i+1}:")
        if masv=="":
            break
        ds.append(masv)
        i+=1
    return ds
def main():
    n=int(input("N="))
    clb=[]
    for i in range(1,n+1):
        print(f"Nhập mã sv cho clb {i}:")
        clb.append(nhap(i))
    K=int(input("K="))
    lopK=set(clb[K-1])
    u=set()
    for i in range(n):
        if i!=K-1:
            u|=set(clb[i])
    print(f"Sv tham gia clb k và tham gia 1 clb khác:",lopK&u)
    dem={}
    for ds in clb:
        for sv in ds:
            if sv not in dem:
                dem[sv]=1
            else:
                dem[sv]+=1
    nhieu=[]
    for sv,solan in dem.items():
        if solan>1:
            nhieu.append(sv)
    print(f"Sv  tham gia nhiều clb khác:",nhieu)
main()
