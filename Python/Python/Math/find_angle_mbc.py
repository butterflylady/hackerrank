import math

ab=int(input())
bc=int(input())
theta=int(round(math.degrees(math.atan(ab/bc)),0))
print(str(theta)+"°")