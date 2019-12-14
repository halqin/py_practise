pi_ = input()
import math
result = [(math.sin(math.radians(int(i)*36)), math.cos(math.radians(int(i)*36))) for i in pi_ if i.isdigit()]
x = sum([i[0] for i in result])
y = sum([i[1] for i in result])
print("Number {} walks to position ({:.02f}, {:.02f}).".format(pi_, x, y))