''' Demonstrate how variables are created and how they work
Author: Arthur Brook
11/04/25
v.1.0'''

#different types of variables
#store a number
my_number = 34.5 #assigned 34.5 to my_number
print(my_number)

my_number = 80 #reassigned the value of my_number
print(my_number)

name1 = "Arthur"
print(name1)

my_number = name1
print(my_number)

"""Now I can
press 
enter 
as
many
times
 as 
 I want"""

sum = 5 + 17 #not good practice
print(sum)

num_1 = 5
num_2 = 17
sum1 = num_1 + num_2 #better practice, more pythonic
print(sum1)

sum_string = "5 + 17 = 22" #this prints everything
print(sum_string)

print(num_1,"+",num_2,"=",sum1)

sum_string1 = "17" #stores a string
sum_string2 = "5"

sum = sum_string1 + sum_string2 #adding sums together is called concatenation
print(sum)

print(f"My calculation for {sum_string1} + {sum_string2} = {sum1}")