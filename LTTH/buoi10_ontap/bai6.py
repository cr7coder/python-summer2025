
def tongam(ds):
    tong=0
    for x in ds:
        if x<0:
            tong+=x
    somin=min(ds)
    somax=max(ds)
    return tong,somin,somax
n=(input("n="))
ds=[float(x) for x in n.split(",")]
u,a,b=tongam(ds)
print(f"Tong am =",u)
print(f"Min =",a)
print(f"Max =",b)

