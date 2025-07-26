# def XEPLOAI(diem):
#     if diem<2:
#         result = "Yếu"  
#     elif diem<2.5:
#         result="TB"
#     elif diem<3.2:
#         result="K"
#     elif diem <3.6:
#         result ="G"
#     else:
#         result="SX"

#     return result

# try:
#     diem = float(input("Diem TL: "))
#     assert diem >=0 and diem <=4,"Điểm không hợp lệ!"
#     print("Xếp loại: ",XEPLOAI(diem))
# except AssertionError as error:
#     print(error)
# except ValueError:
#     print("Điểm phải là số !")
def XEPLOAI(diem):
    if diem<2:
        result="yếu"
    elif diem <2.5:
        result ="trung bình"
    elif diem <3.2:
        result ="khá"
    elif diem <3.6:
        result="giỏi"
    else:
        result="xuất sắc"
    return result
try:
    diem=float(input("Diem TL: "))
    assert diem >=0 and diem <=4,f"Điểm không hợp lệ"
    print("Xếp loại:",XEPLOAI(diem))
except AssertionError as error:
    print(error)
except ValueError:
    print("Điểm phải là số")