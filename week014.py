r1 = float(input())
r2 = float(input())
r_max = max(r1, r2)
r_min = min(r1, r2)

percent = r_max**2/r_min**2
n = int(0.83*percent - 1.9)

print('{} smaller circles cover {:.2f}% of the larger circle'.format(n, 100*n/percent))