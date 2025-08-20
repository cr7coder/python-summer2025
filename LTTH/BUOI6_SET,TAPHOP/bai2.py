def nhap(ten):
    tap=set()
    n=int(input(f"So nhan vien tham gia dự án {ten}:"))
    for i in range(n):
        manv=input(f"MãNV {i+1} :")
        tap.add(manv)
    return tap
A=nhap("A")
B=nhap("B")
cahai=A&B
print(f"Manv tham gia ca 2 dụ án:",cahai)
print(f"Mã nv chi tham gia 1 dự án:",A^B)
print(f"Mã nv tham gia B mà k tham gia A:",B-A)

# def nhap(ten):
#     ds=set()
#     n=int(input(f"So nhan vien tham gia du an {ten}: "))
#     for i in range(n):
#         manv=(input(f"Mã nhân viên {i+1} ({ten}):"))
#         ds.add(manv)
#     return ds
# duanA=nhap("A")
# duanB=nhap("B")
# cahai=duanA & duanB
# print("mnv tham gia ca 2 du an: ",cahai)
# khac=duanB-duanA
# print("tham gia b, k tham gia A:",khac)
# mot=duanB^duanA
# print("tham gia 1 du an",mot)
# xoa=input("Nhap:").strip()
# duanA.discard(xoa)
# duanB.discard(xoa)
# print("Danh sách nhân viên dự án A sau khi xóa:", duanA)
# print("Danh sách nhân viên dự án B sau khi xóa:", duanB)



