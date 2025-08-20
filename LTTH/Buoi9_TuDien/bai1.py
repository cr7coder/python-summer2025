# def nhap_nv(n):
#     return {input(f"Mã NV {i+1}: "): float(input("Lương: ")) for i in range(n)}

# def them_nv(d):
#     k = input("Nhập mã NV cần thêm: ")
#     if k in d:
#         print(f"Mã {k} đã tồn tại. Không thêm.")
#     else:
#         d[k] = float(input("Nhập lương mới: "))
#         print(f"Đã thêm nhân viên {k}.")

#     print("Từ điển sau khi thêm:")
#     print(d)

# def xoa_nv(d):
#     k = input("Nhập mã NV cần xóa: ")
#     if k in d:
#         d.pop(k)
#         print(f"Đã xóa nhân viên {k}.")
#     else:
#         print(f"Không tìm thấy nhân viên {k}.")

#     print("Từ điển sau khi xóa:")
#     print(d)
# def nv_luong_thap_nhat(d):
#     minL = min(d.values())
#     print("NV lương thấp nhất:")
#     for k in d:
#         if d[k] == minL:
#             print(k)

# try:
#     n = int(input("N = "))
#     assert n > 0

#     dsnv = nhap_nv(n)
#     print("Từ điển ban đầu:")
#     print(dsnv)

#     them_nv(dsnv)
#     xoa_nv(dsnv)
#     nv_luong_thap_nhat(dsnv)

# except (ValueError, AssertionError):
#     print("Lỗi: N phải là số nguyên dương.")
def nhap(n):
    nv={}
    for i in range(n):
        while True:
            manv=input(f"MNV {i+1}:")
            luong=float(input(f"Lương {manv}:"))
            nv[manv]=luong
            break
    return nv
def them(nv):
    manv=input("Nhap ma nv can them:")
    if manv in nv:
        print("Mã nhân viên đã tồn tại, không thêm được")
    else:
        luongmoi=float(input(f"Lương mới:"))
        nv[manv]=luongmoi
        print("DSNV SAU KHI THEM")
        for manv,luongmoi in nv.items():
            print(f"MãNV  {manv} --- Lương {luongmoi}")
def luongmin(nv):
    if not nv:
        print("Ma nv k ton tai")
        return
    else:
        minluong=min(nv.values())
        maxluong=max(nv.values())
        print("Nv co luong k  nho nhat cx k lon nhat")
        for manv,luong in nv.items():
            if luong!=minluong and luong !=maxluong:
                print(f"MãNV  {manv} --- Lương {luong}")
def xoa(nv):
    manv=input("Nhap ma nv can xoa:")
    if manv in nv:
        del nv[manv]
        print("DSNV SAU KHI XOA")
        for manv,luong in nv.items():
            print(f"MãNV  {manv} --- Lương {luong}")
    else:
        print("k co mnv")
def main():
    n=int(input("n="))
    dsnv=nhap(n)
    print("DSNV:",dsnv)
    for manv,luong in dsnv.items():
        print(f"MãNV  {manv} --- Lương {luong}")
    them(dsnv)
    luongmin(dsnv)
    xoa(dsnv)
main()
    
    
