def KTRASNT(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def createList():
    A = []
    B = []
    C = set()
    i = 1
    while True:
        dl = input(f"DL-{i} = ")
        if dl == "":
            break
        try:
            number = int(dl)
            A.append(number)
        except ValueError:
            try:
                number = float(dl)
                B.append(number)  # ✅ đúng kiểu float
            except ValueError:
                C.add(dl)
        i += 1
    return A, tuple(B), C

def main():
    A, B, C = createList()
    print("A =", A, "| SL SNT là:", len([i for i in A if KTRASNT(i)]))
    # print ("A=",A,"SL SNT ":,len(x for x in A if KTRASNT(x)))

    if B:
       print(f"Vị trí max trong B:{[i for i in range(len(B)) if B[i]==max(B)]}")
    else:
        print("B = ∅ | Max = None | Vị trí = []")

    if C:
        mx, mn = max(C), min(C)
        print(f"So pt max trong C:{sum(1 for x in C if x==mx)}")
        print(f"So pt min trong C:{sum(1 for x in C if x==mn)}")
    else:
        print("C = ∅ | Max/Min = 0")

main()
