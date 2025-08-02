s=input("Dãy số: ")
s=s.split(",")
ds=[int(x) for x in s ]
print("So phan tu khac nhau a: ",len(set(ds)))
for x in sorted(set(ds)):
    print(f"sô lần xuát hiện của {x} la:",ds.count(x))
x=int(input("X="))
dem=0
for i in range(len(ds)):
    for j in range(i+1,len(ds)):
        if ds[i]+ds[j]==x:
            dem+=1
print(f"So cap co tong = {x} la: ",dem)