def nhap(i):
    ds=[]
    i=0
    while True:
        msv=input(f"MaSV {i+1}: ")
        if msv=="":
            break
        ds.append(msv)
        i+=1
    return ds

# def nhap(i):
#     ds = []
#     i=0
#     while True:
#         i+=1
#         msv = input(f"Msv-{i}: ")
#         if msv == "":
#             break
#         ds.append(msv)
#     return ds
def main():
    try:
        n=int(input("NHạp số lớp học:"))
        lop=[]
        for i in range(1,n+1):
            print(f"Lớp học thứ {i}:")
            lop.append(nhap(i))
        M=int(input("M="))
        N=int(input("N="))
        assert M>0 and N>0,f"M,N phải lớn hơn 0"
        lopM=set(lop[M-1])
        lopN=set(lop[N-1])
        u=lopM-lopN
        k=lopM^lopN
        print(f"Sv tham gia lớp M mà k tham gia lớp N là:",u)
        print(f"SV k tham gia đồng thời cả 2 lớp M,N la:",k)
    except ValueError:
        print("dqfke")
main()
# def main():
#     try:
#         n = int(input("Số lớp: "))
#         lop = []
#         for i in range(1, n+1):
#             print(f"SV lớp {i}")
#             lop.append(nhap(i))
#         M = int(input("Nhập chỉ số lớp M: "))
#         N = int(input("Nhập chỉ số lớp N: "))
#         assert 1 <= M <= n and 1 <= N <= n, "Chỉ số lớp không hợp lệ"
#         lopM = set(lop[M-1])
#         lopN = set(lop[N-1])
#         u = lopM - lopN
#         # tatca = {sv for l in lop for sv in l}
#         # khong_MN = tatca - (lopM | lopN)
#         k=lopM^lopN
#         print("DS SV chỉ tham gia lớp M mà không tham gia lớp N:", u)
#         print("DS SV không tham gia đồng thời cả 2 lớp M và N:", k)

#     except AssertionError as e:
#         print(e)
#     except ValueError:
#         print("Nhập sai dữ liệu")

# main()
