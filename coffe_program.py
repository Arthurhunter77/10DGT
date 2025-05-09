"""Demonstrate how to use while loops and if statements
Arthur Brook
9 May 2025
v.1.0"""

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