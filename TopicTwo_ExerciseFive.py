# Write a program to find the middle of three numbers.
# The program should ask a user to enter three numbers which should be stored into three variables namely A, B and C.
# The program then finds and displays the middle number.

def exerciseFive ():
    #getting three numbers from the user
    A = int(input("Please enter a number: "))
    B = int(input("Please enter another number: "))
    C = int(input("Please enter one more number: "))

    numbers = [A, B, C]  #making the numbers into a list/array

    numbers.sort()  #sorting the list from lowest to highest
    middleNumber = numbers[1] #getting the second number from the list
    print("The middle number is:", middleNumber) #output

exerciseFive()