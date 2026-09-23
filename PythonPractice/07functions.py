# functions.py

def convert_c_to_f(motor_temperature):
    fahrenheit = motor_temperature * 9 / 5 + 32
    return fahrenheit

def describe_temperature(motor_temperature, unit="C"):
    if unit == "F":
        value = convert_c_to_f(motor_temperature)
        label = "F"
    else:
        value = motor_temperature
        label = "C"

    return f"{value:.1f}°{label}"

print(describe_temperature(20))
print(describe_temperature(20, unit="F"))

def robot_speak(name, times=1):
    for _ in range(times):
        print(f"Hello, I am {name}!")

robot_speak("BonicBot")
robot_speak("BonicBot", times=3)
