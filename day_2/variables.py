import math,keyword
# keyword tells the keyword that are reserverd
#'Day 2: 30 Days of python programming
first_name = "Ashmit"
last_name = "Sharma"
full_name = "ASHMIT SHARMA"
country ="INDIA"
city = "CHENNAI"
age = 22
year = 2026
is_married = False
is_true = "yes"
is_light_on = True
name , age , height = 'Ashmit',23,5.6

# LEVEL - 2
# 1. Data type of all variables

first_name = "Ashmit"
last_name = "Sharma"
full_name = "ASHMIT SHARMA"
country = "INDIA"
city = "CHENNAI"
age = 22
year = 2026
is_married = False
is_true = "yes"
is_light_on = True

name, age, height = "Ashmit", 23, 5.6

# Checking data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(height))

len_ofirst_name = print(len(first_name))
len_oflast_name = print(len(last_name))
print(len_ofirst_name==len_oflast_name)
num_one = 5
num_two = 4
variable_total = num_one+num_two
variable_diff = num_two-num_one
variable_product = num_two*num_one
variable_division = num_two/num_one
variable_remainder = num_two%num_one
variable_exp = num_one**num_two
variable_floor_division = num_two//num_one
# CIRCLE

radius = 5
area_of_circle = math.pi*radius**2
print(area_of_circle)

circumference_of_circle = 2*math.pi*radius

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

help('keywords')