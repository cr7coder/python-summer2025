s = input("Nhập dãy số nguyên: ")
s = s.split(",")
ds = [int(x) for x in s]
u = [] 
dem=0
for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if (ds[i] + ds[j]) % 5 == 0:  
            cap = set(sorted((ds[i], ds[j])))
            dem+=1
            u.append(cap)
print("Các cặp thỏa mãn:", u)
print("sl:", dem)