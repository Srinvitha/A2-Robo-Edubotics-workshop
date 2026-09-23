# variables_and_io.py 
  
# Variables and core data types 
robot_name = "BonicBot"       # str 
build_year = 2026              # int 
robot_height = 0.80            # float 
is_active = True               # bool 
  
print(robot_name, build_year, robot_height, is_active) 
print(type(robot_name), type(build_year), type(robot_height), type(is_active)) 
  
# Taking input from the user 
led_color = input("What LED color should the robot use? ") 
print(f"{robot_name} will use {led_color} LEDs.") 
  
# input() always returns a string — even when the user types digits 
startup_year_text = input("What year was the robot built? ") 
startup_year = int(startup_year_text)   # convert str -> int 
current_year = 2026 
years_in_service = current_year - startup_year 
  
print(f"{robot_name} has been in service for approximately {years_in_service} years.")