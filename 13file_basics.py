# file_basics.py

robot_logs = ["startup complete", "obstacle detected", "returning to base"]

with open("robot_log.txt", "w") as f:
    for log_entry in robot_logs:
        f.write(log_entry + "\n")

with open("robot_log.txt", "r") as f:
    content = f.read()

print(content)

with open("robot_log.txt", "r") as f:
    for line in f:
        print(f"Robot log: {line.strip()}")

with open("robot_log.txt", "a") as f:
    f.write("shutdown complete\n")

with open("robot_log.txt", "r") as f:
    all_lines = f.readlines()

print(all_lines)
