def nhap(n):
    dict={}
    for i in range(n):
        key=input(f"MãSV {i+1}:")
        value=float(input("Diem"))
        dict[key]=value
    return dict
def them(dict):
    key=input(f"Nhap ma sv:")
    if key in dict:
        print("MãNV đã tồn tại!!.Khoogn thêm được")
    else:
        diemmoi=0
        dict[key]=diemmoi
        print("DSSV sau khi thêm:")
        for key,diemmoi in dict.items():
            print(f"MãSV: {key} --- Điểm: {diemmoi}")
def main():
    n=int(input("Nhập n="))
    dssv=nhap(n)
    print("DSSV:",dssv)
    for key,value in dssv.items():
        print(f"MãSV: {key} --- Điểm: {value}")
    them(dssv)
    print("DSSV GIAM DAN")
    # dssvgiamdan=sorted(dssv.items(),key=lambda item:item[1],reverse=True)
    diemgiam=sorted(dssv.items(),key=lambda x:x[1], reverse=True )
    for key,value in diemgiam:
            print(f"MãSV: {key} --- Điểm: {value}")

main()

