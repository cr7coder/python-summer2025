# def LOICHAO(tuoi,gt):
#     if tuoi <= 18:
#         lc = 'Em'
#     elif tuoi <= 40:
#         if gt == 'nam':
#             lc = 'Anh'
#         elif gt == 'Nữ':
#             lc = 'Chị'
#     elif tuoi <= 60:
#         lc = 'Bác'
#     else:
#         if gt == 'nam':
#             lc = 'Ông'
#         elif gt == 'Nữ':
#             lc = 'Bà'


#     return lc
# try:
#     hoten = (input('Họ tên: '))
#     tuoi = int(input('Tuổi: '))
#     gt = input('Giới tính: ').strip().lower()
#     assert 0 <= tuoi , 'Tuổi không hợp lệ!'
#     print(f'Xin chào "{LOICHAO(tuoi,gt)}": {hoten}')
# except AssertionError as error:
#    print(error)
# except ValueError:
#     print('Tuổi phải là một số !')
def LOICHAO(tuoi,gt):
    if tuoi<=18:
        lc='Anh'
    elif tuoi <=40:
        if gt =='Nam':
            lc='Anh'
        elif gt=="Nữ":
            lc='Chị'
    elif tuoi <=50:
        lc='Bác'
    else:
        if gt =='Nam':
            lc='Ông'
        elif gt== 'Nữ':
            lc='Bà'

    return lc
try:
    hoten=(input("Họ tên: "))
    tuoi=int(input("Tuổi: "))
    gt=(input("Gioi tính: "))
    assert tuoi>=0,f"Tuổi không hợp lệ"
    print(f'Xin chào "{LOICHAO(tuoi,gt)}":{hoten} ')
except AssertionError as erorr:
    print(erorr)
except ValueError:
    print("Tuổi phải là một số")