time = 996452
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

print('Days', day)
print('Hours', hour)
print('Minutes', minutes)
print('Seconds', seconds)