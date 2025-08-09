def nhap_nv(n):
    return {input(f"Mã NV {i+1}: "): float(input("Lương: ")) for i in range(n)}

def them_nv(d):
    k = input("Nhập mã NV cần thêm: ")
    if k in d:
        print(f"Mã {k} đã tồn tại. Không thêm.")
    else:
        d[k] = float(input("Nhập lương mới: "))
        print(f"Đã thêm nhân viên {k}.")

    print("Từ điển sau khi thêm:")
    print(d)

def xoa_nv(d):
    k = input("Nhập mã NV cần xóa: ")
    if k in d:
        d.pop(k)
        print(f"Đã xóa nhân viên {k}.")
    else:
        print(f"Không tìm thấy nhân viên {k}.")

    print("Từ điển sau khi xóa:")
    print(d)
def nv_luong_thap_nhat(d):
    minL = min(d.values())
    print("NV lương thấp nhất:")
    for k in d:
        if d[k] == minL:
            print(k)

try:
    n = int(input("N = "))
    assert n > 0

    dsnv = nhap_nv(n)
    print("Từ điển ban đầu:")
    print(dsnv)

    them_nv(dsnv)
    xoa_nv(dsnv)
    nv_luong_thap_nhat(dsnv)

except (ValueError, AssertionError):
    print("Lỗi: N phải là số nguyên dương.")
