class Robot:
    def __init__(self, name, battery_levels):
        self.name = name
        self.battery_levels = battery_levels

    def average_battery(self):
        return sum(self.battery_levels) / len(self.battery_levels)

    def summary(self):
        return f"{self.name}: average battery {self.average_battery():.1f}%"

bonicbot = Robot("BonicBot", [82, 91, 76])
robot_a2 = Robot("Robot A2", [70, 65, 80])

print(bonicbot.summary())
print(robot_a2.summary())

robots = [bonicbot, robot_a2]

for robot in robots:
    print(robot.name, robot.average_battery())
