'''Rectangular fence cost calculator
28/05/25
Arthur Brook
v.1.0'''

 #recycling numcheck from AP basics
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

print("Hello! This program will help you calculate the cost of fencing a rectangular area. All measurements to be inputted in meters.")
#keep_going loop recycled from AP basics
keep_going = ""
while keep_going == "":
    #collects neccesary data
    width = numcheck("What is the width of your area? \n")
    length = numcheck("What is the length of your area? \n")
    cost = numcheck("How much does a meter of your fence cost? \n$")
    #runs calculations
    perimeter = round((2*(width+length)),2)
    price = round((perimeter*cost),2)
    print(f"This are has a {perimeter} meter perimeter. It will cost ${price} to fence it all.")

    #user chooses to end program or repeat
    keep_going = input("Do you want to end the program or continue? Press enter to repeat, or anything else to terminate. \n")
print("Thank you for using this program!")


