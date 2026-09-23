class Robot:
    def __init__(self, name):
        self.name = name

    def action(self):
        return f"{self.name} performs an action."

class HumanoidRobot(Robot):
    def action(self):
        return f"{self.name} waves its hand."

class ServiceRobot(Robot):
    def action(self):
        return f"{self.name} performs a service task."

robots = [
    HumanoidRobot("BonicBot"),
    ServiceRobot("ServiceBot"),
    Robot("Generic Robot")
]

for robot in robots:
    print(robot.action())

print(isinstance(HumanoidRobot("BonicBot"), Robot))
