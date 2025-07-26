def KTRASNT(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

try:
    n = int(input("N =  "))
    assert n > 0, "Phải nhập số nguyên dương!"
    
    B = tuple(i for i in range(2, n) if KTRASNT(i))
    
    print(f"Các số nguyên tố nhỏ hơn {n} là:")
    print(B)

except ValueError:
    print("n phải nguyên")
except AssertionError as e:
    print(e)
