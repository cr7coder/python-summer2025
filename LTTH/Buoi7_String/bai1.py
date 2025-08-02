s= input("S:")
print("So ký tự trong xâu la:",len(s.split()))

s="".join(s.split())
print("Chuẩn hóa s:",s)
print("Số lần xuất hiện các kí tự:")
for x in sorted(set(s)):
    print(f"so lan xuat hiện kí tự {x}:",s.count(x))
s=''.join(x for x in s if not x.isdigit())
print("Xau sau khi loai bo chu so:",s)
print("Cac ki tu chi xuat hien 1 lan:")
print(", ".join(x for x in s if s.count(x)==1))
u=s.split()
max_len = max(len(x) for x in u)
print("Các từ dài nhất trong xâu là:")
print(", ".join(x for x in u if len(x) == max_len))
chucai_kyhieu=0
for x in s:
    if(x.islower() or (not x.isupper() and not x.isdigit()and not x.isspace())):
        chucai_kyhieu+=1
print(chucai_kyhieu)