# bounce.py
#
# Exercise 1.5
origin_height = 100

for i in range(10):
    origin_height = origin_height * 3 / 5
    print(i + 1, round(origin_height,4))