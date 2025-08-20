s=input("day:")
s=s.split(",")
ds=[x for x in s]
print("So luong tu trong danh sach:",len(ds))
m=min(len(x) for x in ds)
a=max(len(x) for x in ds)
u=[x for x in ds if len(x)!=m and len(x)!=a]
u.sort()
print("Day la:",u)
