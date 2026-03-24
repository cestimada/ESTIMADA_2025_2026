s = float(input("Give me the speed: "))
d = 42.195
def time(d, s):
    h = d / s
    hours = int(h)
    return hours
def minutes(d, s):
    h = d / s
    fractional = h - int(h)
    m = fractional * 60
    return int(m)
print("At", s, "km/h, it will approximately",
      time(d, s), "hours and",
      minutes(d, s), "minutes to finish a marathon")