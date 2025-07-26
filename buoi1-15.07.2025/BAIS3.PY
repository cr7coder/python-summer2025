import math
def tinhtong(n):
    s = 0
    for i in range(1, n + 1):
        s += ((-1) ** (i - 1)) * i / math.factorial(i)
    return s
try:
    n = int(input("N = "))
    assert n >=2,f"{n} không hợp lệ!"
    ket_qua = tinhtong(n)
    print(f"S{n} = {ket_qua}")
except AssertionError as error:
    print(error)
except ValueError:
    print("N phải là số !")