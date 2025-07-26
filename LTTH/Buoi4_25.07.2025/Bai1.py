
from math import isqrt


def createList(a, b, c, n):
    ds = []
    for x in range(1, isqrt((n - c) // a) + 1):
        for y in range(1,isqrt((n - c - a*x*x) // b) + 1):
            if a*x*x + b*y*y + c < n:
                ds.append((x, y))
    return ds

n = int(input("N = "))
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
ds = createList(a, b, c, n)
print("Các nghiệm (x, y) thỏa F(x, y) < n là:", ds)
print("Tổng số nghiệm:", len(ds))