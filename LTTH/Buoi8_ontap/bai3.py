def ktrascp(x):
    return int(x**0.5)**2==x
def fibonaci(x):
    return ktrascp(5*x*x+4) or ktrascp(5*x*x-4)
def tong(n):
    s=0
    for i in range(1,n+1):
        if fibonaci(i):
            s+=i
    return s
def ucln(m, n):
    while n:
        m, n = n, m % n
    return m
def bcnn(n,m):
    return m*n//ucln(m,n)
def main():
    try: 
        n=int(input("N="))
        m=int(input("M="))
        assert n>0 and m>0,f"N,M Phải dương"
        tongfibo=tong(n)
        print(f"Tong của các số fibonaci nhỏ hơn {n} la:",tongfibo)
        print("UCLN: ",ucln(m,n))
        print("BCNN: ",bcnn(m,n))
    except AssertionError as e:
        print(e)
    except ValueError:
        print("n,m phải nguyen dương")
main()