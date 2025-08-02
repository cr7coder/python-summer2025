def nhap(ten):
    ds=set()
    n=int(input(f"So nhan vien tham gia du an {ten}: "))
    for i in range(n):
        manv=(input(f"Mã nhân viên {i+1} ({ten}):"))
        ds.add(manv)
    return ds
duanA=nhap("A")
duanB=nhap("B")
cahai=duanA & duanB
print("mnv tham gia ca 2 du an: ",cahai)
khac=duanB-duanA
print("tham gia b, k tham gia A:",khac)
mot=duanB^duanA
print("tham gia 1 du an",mot)
xoa=input("Nhap:").strip()
duanA.discard(xoa)
duanB.discard(xoa)
print("Danh sách nhân viên dự án A sau khi xóa:", duanA)
print("Danh sách nhân viên dự án B sau khi xóa:", duanB)


# def nhap_nhanvien(ten_duan):
#     ds = set()
#     n = int(input(f"Nhập số nhân viên của dự án {ten_duan}: "))
#     for i in range(n):
#         ma = input(f"Mã nhân viên {i+1} ({ten_duan}): ").strip()
#         ds.add(ma)
#     return ds
# duanA = nhap_nhanvien("A")
# duanB = nhap_nhanvien("B")
# giao = duanA & duanB
# print("\nMã nhân viên tham gia cả 2 dự án:", giao)

# khac = duanB - duanA
# print("Mã nhân viên tham gia dự án B mà không tham gia dự án A:", khac)

# chi_mot_duan = duanA ^ duanB
# print("Mã nhân viên chỉ tham gia một dự án:", chi_mot_duan)

# xoa = input("\nNhập mã nhân viên cần xóa khỏi cả hai dự án: ").strip()
# duanA.discard(xoa)
# duanB.discard(xoa)

# print("Danh sách nhân viên dự án A sau khi xóa:", duanA)
# print("Danh sách nhân viên dự án B sau khi xóa:", duanB)
