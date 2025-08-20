def scp(x):
    return int(x**0.5)**2==x
def ktrascp(n,m):
    a=set()
    for x in range(min(n,m),max(n,m)+1):
        if scp(x) and x%2==0:
            a.add(x)
    return a
def main():
    try:
        n=int(input("N="))
        m=int(input("M="))
        assert n>0 and m>0, f"N,M phải nguyên dương"
        a=ktrascp(n,m)
        print("SCP chan la:",a)
    except AssertionError as e:
        print(e)
    except ValueError:
        print("N,M phải là số")
main()