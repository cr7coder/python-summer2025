# def tinhtong(n):
    
#     s = 0
#     for i in range(1, n):
#         s += (i) / (i+1) 
#         #for i in range(2, n+1):
#         #s += (i-1) / (i) 
#     return s
# try:
#     n = int(input("N = "))
#     assert n >=2,f"{n} không hợp lệ!"
#     ket_qua = tinhtong(n)
#     print(f"S{n} = {ket_qua}")
# except AssertionError as error:
#     print(error)
# except ValueError:
#     print("N phải là số !")
def tong(n):
    s=0
    for i in range(2,n+1):
        s+=(i-1)/(i)
    return s
def main():
    try:
        n= int(input("N = "))
        assert n>=2,f"{n} không hợp lệ!!"
        ketqua=tong(n)
        print(f"S{n}= {ketqua:.6f}")
    except AssertionError as r:
        print(r)
    except ValueError:
        print("n phải là số")

main()