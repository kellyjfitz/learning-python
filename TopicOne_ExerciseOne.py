def exercise_one ():
    pound_weight = float(input("Enter the weight of an object in pounds: "))
    kilo_weight = pound_weight * 0.454 #doing the conversion
    print("The weight of the object in kilograms is " ,kilo_weight,"kg", sep='')
exercise_one()

def exercise_two ():
    celsius_temp = int (input("Please enter a temperature in Celsius for conversion: "))
    fahrenheit_temp = (9/5) * celsius_temp + 32 #doing the conversion
    print(celsius_temp, " degrees Celsius is ", int(fahrenheit_temp),"F", sep='')
exercise_two()

def exercise_three ():
    #entering figures for buy transaction
    initial_purchase_number = 500
    initial_price_per_share = 25.04
    initial_commission = 0.023

    #calculating the cost and commission of the buy transaction
    initial_buy_total = initial_purchase_number * initial_price_per_share
    initial_commission_value = initial_buy_total * initial_commission
    
    #entering figures for sell transaction
    stocks_sold = 500
    sale_price_per_share = 36.06
    sale_commission = 0.021

    #calculating total and commission of sale transaction
    sale_total = stocks_sold * sale_price_per_share
    sale_commission_value = sale_total * sale_commission

    #adding together the buy cost, buy comission and sale commission to get total outlay
    #converting to a float for accuracy
    total_outlay = float(initial_buy_total + initial_commission_value + sale_commission_value)

    #calculating profit by subtracting total outlay from the sale total
    profit = sale_total - total_outlay

    #outputting the figures
    print ("Bought : ", initial_buy_total)
    print ("Commission paid on purchase: $", initial_commission_value)
    print("Sold stock for: $", sale_total)
    print("Commission on sale: $", sale_commission_value)
    
    #formatting profit to two decimal places
    print("Net profit: $", format(profit, '.2f')) 

exercise_three()
