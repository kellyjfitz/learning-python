# Write a program that asks the user to enter an integer. The program should display 'Positive' if the number is greater than 0, 'Negative' if the number is less than 0, and 'Zero' if the number is equal to 0. The program should then display 'Even' if the number is even, and 'Odd' if the number is odd.

def exerciseOne ():
    user_number = int(input("Please enter an integer: "))
    if user_number >0:
        print("Positive")
    elif user_number == 0: print ("Zero")
    else: print("Negative")
    if user_number % 2 == 0:
        print ("Even")
    else: print ("Odd")

exerciseOne()