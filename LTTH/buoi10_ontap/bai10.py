s=input("Day so:")
ds = [float(x) for x in s.split()]
soam = [x for x in ds if x < 0]
soduong = [x for x in ds if x > 0]
print("Số âm lớn nhất :",  [x for x in soam if x== max(soam)])
print("Số dương nhỏ nhất :", tuple(x for x in soduong  if x == min(soduong)))
