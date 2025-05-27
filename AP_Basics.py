'''Area/Perimeter Basics
21/05/25
Arthur Brook
v.1.0
fav_num = 7
num_string = "5"
print(fav_num*2)
print(num_string*5)

love_programming = True
greeting = 'hello world'
print(f"{greeting}! my favorite number is {fav_num}, and it is {love_programming} that I love programming.")
'''


'''username = input("What is your name? ")
fav_num = int(input("What is your favorite number? "))

half = fav_num / 2
double = fav_num * 2
square = fav_num ** 2

print(f"Hi {username}, your favorite number is {fav_num}.")

print(f"Double {fav_num} is {double}.")
print(f"Half of {fav_num} is {half}.")
print(f"{fav_num} squared is {square}. \n \nHave a nice day!")'''

#area and perimeter
#ask user for width and length until they provide a number larger than 0
 
def numcheck(question):
    #numcheck function runs the code to get a valid number from the user
    error = "Please enter a number that is more than zero.\n"
    keep_going = ""
    while keep_going == "":

        try:
            response = float(input(question))

            if response > 0:
                keep_going = 'nope'
            else:
                print(error)
        except:
            print(error)
    return response

'''for item in range(0,2):
    width = numcheck("Width: ")
    print(width)

for item in range(0,2):
    height = numcheck("Width: ")
    print(height)'''
keep_going = ""
while keep_going == "":
    width = numcheck("Width: ")
    print(width)

    height = numcheck("Height: ")
    print(height)
    #just simple math calculations
    area = round((width * height),2)
    print(f"The area of a rectangle with these sides is {area}.")
    perimeter = round(((width*2)+(height*2)),2)
    print(f"The perimeter of a rectangle with these sides is {perimeter}.")
    #if enter, keep_going remains the same. if anything else, keep_going changes and ends the loop
    keep_going = input("Do you want to continue the program? Press enter to continue, or any other key to terminate. ")