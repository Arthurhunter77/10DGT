"""Demonstrate how to use while loops and if statements
Arthur Brook
9 May 2025
v.1.0"""
'''
#while loop
keep_going = "" #the variable contains an empty string
while keep_going == "":

    like_coffee = input("Do you like coffee? \n")

    if like_coffee == "yes":
        print("That is great. I like coffee too!")
        keep_going = "gunshot"
    elif like_coffee == "no":
        print("Well, well, well. I'm sorry for you, then. Termination sequence, initiated.")
        keep_going = "gunshot"
        '''

# v.2.0
#making the program more pythonic
'''keep_going = ""
while keep_going == "":
    #.lower turns answer lowercase
    like_coffee = input("Do you like coffee?\n").lower()
    if like_coffee == "yes" or like_coffee == "y":
        print("Awesome, bro! Same!")
        keep_going = "FINALLY"
    elif like_coffee == "no" or like_coffee == "n":
        print("Wow. I am so sorry for you.")

    

        like_tea = input("Do you at least like tea?\n").upper()

        if like_tea == "YES" or like_tea == "Y":
            print("Well, I guess that's something. You better like coffee by tomorrow, or else.")
            keep_going = "FINALLY"
        elif like_tea == "NO" or like_tea == "N":
            print("You don't like anything? At all? Ha! I caught you, robot!")
            keep_going = "FINALLY"
    else:
        print("I never took basic human vocabulary in preschool. I only learned yes and no.")
    if keep_going == "FINALLY":
        keep_going = input("Press <enter> to continue or any other key to end.")'''
"""v.3.0
14/05/25
Demonstrate how to create functions, thus making my code recyclable

This program asks the user for a number and does something with it.
Loops program until a valid number gets entered"""

def intcheck(question, low, high): #def creates a function, named intcheck
    valid = False
    while not valid:
        error = "Whoops, you have entered an invalid number. Please enter a valid integer between {low} and {high}."

        try:
            response = int(input(f"Enter an integer between {low} and {high}: "))
            

            if low<= response <=high:
                print(f"Your number is {response}.")
                valid = True
            else:
                print(error)
               
        except:
            print(error)
    return response

num1 = intcheck("Enter a number between 1 and 10 ", 1, 10) #calls the function
num2 = intcheck("Enter a number between 15 and 20 ", 15, 20)

sum_num = num1 + num2
multiply = num1 * num2

print(f"Added together, your number are {sum_num}. \n Multiplied, your numbers are {multiply}.")