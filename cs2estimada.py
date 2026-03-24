import math
grav= 9.8
angle=int(input("Enter angle in degrees: "))
distance=int(input("Enter distance in meters: "))
radians=(math.radians(angle))
r=radians*2
sin=(math.sin(r))
ini_velocity= (math.sqrt(distance*grav/sin))
c=round(ini_velocity, 2)
print(f"req launch speed: {c} m/s")