# def tinhtong(n):
#         s = 0
#         for i in range(1, n + 1):
#             s += 2 / (i + 1)
#         return s

# try:
#     n = int(input("N = "))
#     assert n >= 1, f"{n} không hợp lệ!"
#     ket_qua = tinhtong(n)
#     print(f"S{n} = {ket_qua:.4f}")
# except AssertionError as error:
#     print(error)
# except ValueError:
#     print("N phải là số !")
def tong(n):
    s=0
    for i in range(1,n+1):
        s+=2/(i+1)
    return s
def main():
    try:
        n=int(input("N = "))
        assert n>=1,f"{n} không hợp lệ"
        ketqua=tong(n)
        print(f"S{n}= {ketqua}")
    except AssertionError as e:
        print(e)
    except ValueError:
        print("n phải là số")

main()