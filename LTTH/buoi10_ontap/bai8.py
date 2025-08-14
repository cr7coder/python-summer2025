n = int(input("Nhập số lớp trong học kỳ: "))
lop = []
for i in range(1,n+1):
    ds = set(input(f"Nhập mã SV lớp {i+1}: ").split())
    lop.append(ds)

if lop: 
    sv_all = set.intersection(*lop)
    print("Danh sách SV tham gia tất cả các lớp:", sv_all)
else:
    print("Không có lớp nào được nhập.")

m = int(input("Nhập số thứ tự lớp m: "))

sv_lop_m = lop[m]
lop_khac = set().union(*(lop[i] for i in range(1,n+1) if i != m))
A = sv_lop_m.difference(lop_khac)
print("Sinh viên chỉ tham gia lớp m:", A)


ma_sv = input("Nhập mã SV cần kiểm tra: ")
k = int(input("Nhập số thứ tự lớp k: "))
if 1 <= k <= n:
    if ma_sv in lop[k]:
        lop[k].remove(ma_sv)
        print(f"Đã xóa {ma_sv} khỏi lớp {k+1}")
    else:
        lop[k].add(ma_sv)
        print(f"Đã thêm {ma_sv} vào lớp {k+1}")
else:
    print("Số lớp k không hợp lệ.")
