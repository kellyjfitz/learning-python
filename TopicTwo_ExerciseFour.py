# Assume that a retail company awards loyalty points to its customers. The points are calculated based on the total sales (rounded figure) according to the following table.
# Write a program that asks the user to enter the total sales of a customer and then displays the points earned by that customer.
# Total sales  $0-$100, Points 10
# Total sales  $101-$500, Points 20
# Total sales  more than $500, Points 50
def exerciseFour ():
    price = int(float(input("Please enter the sale amount: $"))) #doing this to cope with both int and floats
    if price >=0 and price <= 100:
        points = 10
    elif price >=101 and price <=500:
        points = 20
    elif price >500:
        points = 50
    else: #error handling
        points = "That doesn't look right, please restart the program and try again."
    print("Points earned with this purchase:", points)
exerciseFour()