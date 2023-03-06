# Consider that there are three seating categories at the Mount Panorama Motor Racing Circuit, Bathurst.
# #The categories are Class A, Class B, and Class C. For a motor race, Class A seats cost $50, Class B seats cost $30, and Class C seats cost $15.
# Write a program that asks the user to enter a class of the ticket (A or B or C), and then displays the cost of the ticket.
def exerciseThree():
    classA = 50
    classB = 30
    classC = 15
    ticketPrice = "Your ticket will cost $"

    ticketClass = input("What class of ticket would you like? A, B or C? ")
    if (ticketClass == "A") or (ticketClass == "a"):
        ticketPrice = ticketPrice + str(classA)
    elif (ticketClass == "B") or (ticketClass == "b"):
        ticketPrice = ticketPrice + str(classB)
    elif (ticketClass == "C") or (ticketClass == "c"):
        ticketPrice = ticketPrice + str(classC)
    else:
        ticketPrice = "That doesn't look right. Please rerun the program and try again."

    print(ticketPrice)


exerciseThree()
