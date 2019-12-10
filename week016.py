from math import floor
sol = int(input())
sol_sec = 24*3600+39*60+35.244
total_time = sol*sol_sec
d = floor(total_time/(24*3600))
h = floor(total_time%(24*3600)/3600)
m = floor((total_time-d*24*3600-h*3600)/60)
s = int(total_time-d*24*3600-h*3600-m*60)

print('{} sols = {} days, {} hours, {} minutes and {} seconds'.format(sol, d,h,m,s))

