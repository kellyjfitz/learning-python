# Consider that there are three seating categories at the Mount Panorama Motor Racing Circuit, Bathurst. The categories are Class A, Class B, and Class C. For a motor race, Class A seats cost $50, Class B seats cost $30, and Class C seats cost $15.
# Write a program that asks the user to enter a class of the ticket (A or B or C), and then displays the cost of the ticket.
def exerciseThree():
    classA = 50
    classB = 30
    classC = 15
    userQuestion = "What class of ticket would you like? A, B or C? "
    ticketPrice = 0
    
    ticketClass = input(userQuestion)
    if ticketClass == "A" or "a": 
        ticketPrice = classA
    elif ticketClass == "B" or "b":
        ticketPrice = classB
    elif ticketClass == "C" or "c":
        ticketPrice = classC
    else: ticketClass = "WWWWWWW"
    
    print("Your ticket will cost $", ticketPrice, sep="")

exerciseThree()

# Assume that a retail company awards loyalty points to its customers. The points are calculated based on the total sales (rounded figure) according to the following table.
# Write a program that asks the user to enter the total sales of a customer and then displays the points earned by that customer.
