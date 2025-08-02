def nhap_tuple():
    lst = []
    i = 1 
    while True:
        try:
            x = int(input(f"So-{i}: "))
            if i == 1 and x == 0:
                return ()
            if x == 0:
                break
            lst.append(x)
            i += 1
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    return tuple(lst)
def main():
    T = nhap_tuple()
    if not T:  
        print("T = ",len())
        return

    print("T =", T)

    if all(n > 0 for n in T):
        print("Tong", sum(T))
    elif any(n > 0 for n in T):
        soam = tuple(n for n in T if n < 0)
        print("L =", soam)
    else:
        tbc = sum(T) / len(T)
        print("TBC:", abs(tbc))

main()
