# def nhap(n):
#     sv={}
#     for i in range(n):
#         while True:
#             masv=input(f"Masv {i+1}:")
#             if masv in sv: 
#                 print("Ma sv đã tồn tại, vui lòng nhập mã khác ")
#             else:
#                 try: 
#                     diem = float(input(f"Điểm:"))
#                     sv[masv]=diem
#                     break
#                 except ValueError:
#                     print("Điểm phải là số")
#     return sv
# # def nhap(n):
# #     nv = {}
# #     for i in range(n):
# #         while True:
# #             manv = input(f"MNV {i+1}: ")
# #             if manv in nv:
# #                 print(f"Mã nhân viên {manv} đã tồn tại. Vui lòng nhập mã khác.")
# #             else:
# #                 try:
# #                     diem = float(input(f"Nhập điểm của {manv}: "))
# #                     nv[manv] = diem
# #                     break
# #                 except ValueError:
# #                     print("Lương phải là số. Nhập lại.")
# #     return nv

# def diemmax(sv):
#     if not sv:
#         print("Sinh vien chua co trong danh sach")
#         return
#     maxdiem=max(sv.values())
#     print("Sinh vien co điểm cao nhất: ")
#     for masv,diem in sv.items():
#         if diem == maxdiem:
#             print(f"Mã: {masv}    Điểm:   {diem}")
# # def diemmax(nv):
# #     if not nv:
# #         print("Không có nhân viên nào trong từ điển")
# #         return
# #     maxdiem = max(nv.values())
# #     print("Nhân viên có điểm cao nhất:")
# #     for ma, diem in nv.items():
# #         if diem == maxdiem:
# #             print(f"Mã: {ma} Lương: {diem}")

# def xoa(sv):
#     masv=input("Nhap ma sv can xoa:")
#     if masv in sv:
#         del sv[masv]
#         print(f"Đã xóa sv!! {masv}")
#     else:
#         print(f"Mã sv {masv} k tồn tại")
# # def xoa(nv):
# #     manv = input("\nNhập mã sinh viên cần xóa: ")
# #     if manv in nv:
# #         del nv[manv]
# #         print(f"Đã xóa sinh viên {manv}.")
# #     else:
# #         print(f"Mã sinh viên {manv} không tồn tại.")
# def main():
#     try:
#         n=int(input("N="))
#         assert n>0,f"N phải lớn hơn 0"
#         dssv=nhap(n)
#         print("Danh sách sv",dssv)
#         print(f"\n{'Mã Sinh Vien'}   {'Điểm'}")
#         for masv,diem in dssv.items():
#             print(f"{masv}   {diem}")
#         diemmax(dssv)
#         xoa(dssv)
#         print("Danh sach sau khi xoa",dssv)
#     except AssertionError as e:
#         print(e)
#     except ValueError:
#         print("N phải la so")
# main()

# # try:
# #     n = int(input("N = "))
# #     assert n > 0, "Không hợp lệ"
# #     dsnv = nhap(n)
# #     print("Danh sách sinh viên",dsnv)
# #     print(f"\n{'MãSV'} {'Điểm'}")
# #     for ma, diem in dsnv.items():
# #         print(f"{ma} {diem}")
# #     diemmax(dsnv)
# #     xoa(dsnv)
# #     print("Danh sách sau khi xóa",dsnv)
# # except AssertionError as e:
# #     print(e)
# # except ValueError:
# #     print("Vui lòng nhập số nguyên dương")

def nhap(n):
    sv={}
    for i in range(n):
        while True:
            masv=input(f"MaSV {i+1}:")
            if masv in sv:
                print("Masv đã tồn tại!!")
            else:
                try:
                    diemtk=float(input(f"Diem tk cua sv {masv}:"))
                    sv[masv]=diemtk
                    break
                except ValueError:
                    print("jdhkjw")
    return sv
def mindiemtk(sv):
            diemmin=min(sv.values())
            print("Sinh vien co diem tk thap nhat:")
            for masv,diemtk in sv.items():
                if diemtk ==diemmin:
                    print(f"MãSV:  {masv}--- Điểm:  {diemtk}")

                
def xoa(sv):
    masv=input("Nhap ma sv can xoa:")
    if masv in sv:
        del sv[masv]
        print(f"Đã xóa sv {masv}")
        print(f"Danh sách sv sau khi xoa:")
        for masv,diemtk in sv.items():
            print(f"MãSV:  {masv}--- Điểm:  {diemtk}")
    else:
        diemmoi=float(input(f"Nhap diem cho sv {masv}:"))
        sv[masv]=diemmoi
        print("Danh sách sv sau khi them:")
        for masv,diemmoi in sorted(sv.items(),key=lambda item:item[1],reverse=True):
            print(f"MãSV:  {masv} --- Điểm:  {diemmoi}")
def main():
    try:
        n=int(input("N="))
        assert n>0,f"N phải lớn hơn 0"
        dssv=nhap(n)
        print("Danh sách sinh viên",dssv)
        for masv,diemtk in dssv.items():
            print(f"MãSV:  {masv} --- Điểm:  {diemtk}")
        mindiemtk(dssv)
        xoa(dssv)
    except ValueError:
        print("dfe")
main()
