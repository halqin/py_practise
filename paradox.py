import  pylabx, y = [], []def alg_a(n):    # n = int(input('input n'))    for j in range(n):        q = 1.0        for i in range(j):            q *= (366 - i)/365    # print(1 - q)        x.append(j+1)        y.append(1-q)    return x, yx, y = alg_a(200)pylab.plot(x,y)pylab.xlim([0,365])pylab.show()