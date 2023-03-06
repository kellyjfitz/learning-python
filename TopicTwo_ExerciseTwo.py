# Write a program to calculate the cost of processing word documents by a computer operator. Assume that typing speed of the operator is 30 words per minute. The operator charges two different rates according to job duration. For 8 hours or less, the cost is $21.75 per hour of labour otherwise the cost is $25 per hour of labour. The program should ask the user to enter the number of words of a document to be typed and display the following data:
# The hours of labour required
# The labour charges

def exerciseTwo ():
    wordsPerMinute = 30.0
    rateOne = 21.75
    rateTwo = 25

    projectWords = int(input("How many words is your project? "))

    #dividing the word total by typing speed to get duration in minutes, 
    #then dividing by 60 to get duration in hours 
    duration = (projectWords / wordsPerMinute) /60.0 
    if duration <= 8:
        projectCost = format(rateOne * duration, ".2f")
    else: projectCost = format(rateTwo * duration, ".2f")

    print("Your project will take ", format(duration, ".1f"), " hours to complete and will cost $", projectCost, sep='')

exerciseTwo()

