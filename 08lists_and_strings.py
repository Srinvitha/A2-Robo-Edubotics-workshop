# lists_and_strings.py

robot_actions = ["walk", "turn", "wave"]
action_steps = [10, 90, 1]

print(robot_actions[0], action_steps[0])  # indexing
print(robot_actions[-1])                 # negative indexing
print(robot_actions[0:2])               # slicing

robot_actions.append("handshake")
action_steps.append(2)

print(robot_actions, action_steps)
print("Number of actions:", len(robot_actions))

# pairing list data with zip + a for loop
for action, steps in zip(robot_actions, action_steps):
    print(f"{action}: {steps} steps")

# basic string manipulation
robot_status = "BonicBot,82,Ready"

parts = robot_status.split(",")

print(parts)

robot_name, battery_text, status = parts

summary = f"{robot_name.upper()} battery {battery_text}% - {status}"

print(summary)

actions_joined = ", ".join(robot_actions)

print("Action sequence:", actions_joined)
