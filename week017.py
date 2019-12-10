hour = int(input())
min_ = int(input())

hour_deg = 360/12
hourmin_deg = hour_deg/60
min_deg = 360/60


hour_angle = hour%12*hour_deg + hourmin_deg*min_
min_angle = min_deg*min_
angle = abs(hour_angle-min_angle)

print("At {:02d}:{:02d} both hands form an angle of {:.1f}°.".format(hour, min_, min(angle, 360-angle)))
