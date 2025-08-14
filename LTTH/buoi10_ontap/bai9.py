def nhap(n):
    dict = {}
    for i in range(n):
            msv = input(f"Nhập mã sinh viên thứ {i+1}: ")
            diem = float(input(f"Nhập điểm tổng kết của {i+1}: "))
            dict[msv] = diem
    return dict
def xuat(dict):
    print("danh sach sv:")
    print(f"MSV  Điểm")
    for msv,diem in dict.items():
        print(f"{msv}  {diem}")


def diemmin(dict):
    min_diem = min(dict.values())
    return [msv for msv, diem in dict.items() if diem == min_diem]

def themmoi(dict):
    new_msv = input("Nhap ma sv: ")
    if new_msv in dict:
        del dict[new_msv]
    else:
        new_diem = int(input("nhap diem moi: "))
        dict[new_msv] = new_diem
    return dict

n = int(input("Nhập số lượng sinh viên: "))
dssv = nhap(n)
xuat(dssv)
sv_min = diemmin(dssv)
print("\nDanh sách mã SV có điểm nhỏ nhất:", sv_min)
dssv = themmoi(dssv)
xuat(dssv)
