def taoL(n):
    A = []  # chứa số
    B = []  # chứa chuỗi
    C=set()
    for i in range(n):
        dl = input(f"Nhập giá trị thứ {i+1}: ")
        try:
            number=int(dl)
            C.add(number)
        except ValueError:
            try:
                number = float(dl)  # nếu nhập được số
                A.append(number)
            except ValueError:
                B.append(dl)  # nếu không phải số thì thêm vào B
    return A,C, B

n = int(input("N = "))
A,C, B = taoL(n)

print("Tổng các phần tử của A =", sum(A))
print("C=",C)
print("Danh sách B =", "-".join(B))
