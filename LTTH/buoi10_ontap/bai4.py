# import math

# x = float(input("x: "))

# if x <= 1:
#     fx = x**2 + 1
#     print(f"f(x) = {x}^2 + 1 = {fx}")
# elif x <= 5:
#     fx = math.log(x) + abs(x + 2)
#     print(f"f(x) = log2({x}) + |{x} + 2| = {fx}")
# else:
#     if x == 0 or x - 5 <= 0:
#         print("k hop le")
#     else:
#         fx = (x - 1) / (x * math.sqrt(x - 5))
#         print(f"f(x) = ({x} - 1) / ({x} * sqrt({x} - 5)) = {fx}")

import math
x=float(input("X="))
if x<=1:
    fx=pow(x,2)+1
    print(f"fx=",fx)
elif x<=5:
    fx=math.log(x)+abs(x+2)
    print(f"fx=",fx)
else:
    fx=(x-1)/(x* math.sqrt(x-5))
    print(f"fx=",fx)
