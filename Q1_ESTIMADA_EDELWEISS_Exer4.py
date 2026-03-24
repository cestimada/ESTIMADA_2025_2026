def c_temp(unit, temp):
    if unit.lower()=="fahrenheit":
      celsius = (temp-32)*5/9
    elif unit.lower()=="kelvin":
      celsius = temp-273.15
    elif unit.lower()== "celsius":
      celsius = temp
    else:
        return "Invalid"
        
        
    if celsius<0:
        return "Too cold!"
    elif 0<= celsius <=35:
        return "Safe temperature"
    else:
        return "Too hot!"
        
        
unit= input("Choose a unit of measurement(celsius, fahrenheit, kelvin):")
if unit.lower() not in ["celsius", "fahrenheit", "kelvin"]:
    print("invalid")
    exit()
temp = float(input("enter temperature:"))


status = c_temp(unit,temp)
print(status)
