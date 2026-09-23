# conditionals.py

battery_level = 82

if battery_level >= 90:
    status = "Excellent"
elif battery_level >= 75:
    status = "Good"
elif battery_level >= 60:
    status = "Low"
else:
    status = "Critical"

print(f"Battery: {battery_level}% -> Status: {status}")

# Comparison and logical operators
motor_temperature = 5
obstacle_detected = True

if motor_temperature < 10 and obstacle_detected:
    print("Obstacle detected. Stop movement.")
elif motor_temperature < 10:
    print("Motor temperature is low.")
elif obstacle_detected:
    print("Obstacle detected.")
else:
    print("Movement is safe.")
