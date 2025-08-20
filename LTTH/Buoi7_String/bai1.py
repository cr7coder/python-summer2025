# s= input("S:")
# print("So ký tự trong xâu la:",len(s.split()))

# s="".join(s.split())
# print("Chuẩn hóa s:",s)
# print("Số lần xuất hiện các kí tự:")
# for x in sorted(set(s)):
#     print(f"so lan xuat hiện kí tự {x}:",s.count(x))
# s=''.join(x for x in s if not x.isdigit())
# print("Xau sau khi loai bo chu so:",s)
# print("Cac ki tu chi xuat hien 1 lan:")
# print(", ".join(x for x in s if s.count(x)==1))
# u=s.split()
# max_len = max(len(x) for x in u)
# print("Các từ dài nhất trong xâu là:")
# print(", ".join(x for x in u if len(x) == max_len))
# chucai_kyhieu=0
# for x in s:
#     if(x.islower() or (not x.isupper() and not x.isdigit()and not x.isspace())):
#         chucai_kyhieu+=1
# print(chucai_kyhieu)

s=input("Xâu:")
ds=[x for x in s]
print("Số từ trong xâu la:",len(s.split()))
chuanhoa="".join(s.split())
print("Chuẩn hóa:",chuanhoa)
print("Số lần xuát hiện của các kí tự:")
for x in sorted(set(s)):
    print(f"Số lần xuất hiện của {x} la: ",s.count(x))
p=' '.join(x for x in s if not x.isdigit())
print("Xâu khi bỏ số la:",p)
z=",".join(x for x in s if s.count(x)==1)
print("Các từ chỉ xuất hiện 1 lần trong sâu la:",z)
k=s.split()
dainhat=max(len(x) for x in k)
u=[x for x in k if len(x)==dainhat]
print("Cac tu dai nhat trong xau la:",u)
chucai_kyhieu=0
for x in s:
    if x.islower()or (not x.isupper() and not x.isdigit() and not x.isspace()):
        chucai_kyhieu+=1
print(chucai_kyhieu)


m=" ".join("@" if x.isupper() else x for x in s)
print(m)
h=s.split()
min_len = min(len(x) for x in h)
kq = " ".join("&" if len(x)==min_len else x for x in h)
print("S: ",kq)