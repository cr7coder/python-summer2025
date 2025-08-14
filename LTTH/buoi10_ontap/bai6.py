def scp(x):
    return int(x**0.5)**2==x
def tongam(ds):
    tong=0
    for x in ds:
        if x<0:
            tong+=x
    somin=min(ds)
    somax=max(ds)
    scpu=[x for x in ds if scp(x)]
    return tong,somin,somax,scpu
n=(input("n="))
ds=[float(x) for x in n.split(",")]
u,a,b,e=tongam(ds)
print(f"Tong am =",u)
print(f"Min =",a)
print(f"Max =",b)
print("SCP:",e)

