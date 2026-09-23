# variables_and_io.py 
  
# Variables and core data types 
name = "Srinvitha"          # str 
age = 20                # int 
height_m = 1.63         # float 
is_student = True       # bool 
  
print(name, age, height_m, is_student) 
print(type(name), type(age), type(height_m), type(is_student)) 
  
# Taking input from the user 
favorite_color = input("What's your favorite color? ") 
print(f"{name} likes {favorite_color}.") 
  
# input() always returns a string — even when the user types digits 
birth_year_text = input("What year were you born? ") 
birth_year = int(birth_year_text)   # convert str -> int 
current_year = 2026 
approx_age = current_year - birth_year 
  
print(f"You're approximately {approx_age} years old.")