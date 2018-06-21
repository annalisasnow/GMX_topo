import math


coord4 = [2.151,   -3.143, 0.248]
coord3 = [3.069857142857143, -0.39985714285714286, -0.3092857142857143]
coord5 = [0.7886666666666667, 0.16516666666666668, 0.5218333333333334]


dist34 = math.sqrt((coord4[0] - coord3[0]) ** 2 + (coord4[1] - coord3[1]) ** 2 + (coord4[2] - coord3[2]) ** 2)
dist54 = math.sqrt((coord4[0] - coord5[0]) ** 2 + (coord4[1] - coord5[1]) ** 2 + (coord4[2] - coord5[2]) ** 2)

print(dist34)
print(dist54)
