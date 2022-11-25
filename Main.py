def startProgram():
    print("\n============================================\n")
    # This is a function that asks the user to input a day of the week that the year begins. It will
    # keep asking the user to input a valid day of the week until the user inputs a valid day of the
    # week.
    startingDayOfYear = int(input("What day of the week the year begins (1 - Sun, 2 - Mon, ..., 7 - Sat): "))
    while(not(startingDayOfYear >= 1 and startingDayOfYear <= 7)):
        print("Day of week is invalid! Please try again.")
        print("\n============================================\n")
        startingDayOfYear = int(input("What day of the week the year begins (1 - Sun, 2 - Mon, ..., 7 - Sat): "))
    
    # This is a function that asks the user to input a month. It will keep asking the user to input a
    # valid month until the user inputs a valid month.
    month = int(input("Choose a month (1 - Jan, 2 - Feb, ..., 12 - Dec): "))
    while(not(month >= 1 and month <= 12)):
        print("Month is invalid! There are 12 month, please try again.")
        print("\n============================================\n")
        month = int(input("Choose a month (1 - Jan, 2 - Feb, ..., 12 - Dec): "))

    # This is a function that asks the user to input a day from the given month. It will keep asking
    # the user to input a valid day from the given month until the user inputs a valid day from the
    # given month.
    dayFromMonth = int(input("Choose a day from the given month: "))
    while(not(dayFromMonth <= getMonthDays(month))):
        print(getMonthName(month) + " only have " + str(getMonthDays(month)) + " days! Please try again.")
        print("\n============================================\n")
        dayFromMonth = int(input("Choose a day from the given month: "))
    print("\n============================================\n")

    # Calling the function `generateCalendar` with the parameters `startingDayOfYear`, `month`, and
    # `dayFromMonth`.
    generateCalendar(startingDayOfYear, month, dayFromMonth)

"""
This function takes in the starting day of the year, the month, and the number of days in the month,
and prints out a calendar for that month

:param startingDayOfYear: The day of the year that the month starts on
:param month: The month you want to display
:param dayFromMonth: The number of days in the month
"""
def generateCalendar(startingDayOfYear, month, dayFromMonth):
    printMonth(month)
    displayCalendar(startingDayOfYear, month, dayFromMonth)
    print("\n\n============================================\n")

"""
It returns the name of the month, given the month number

:param month: The month number (1-12)
:return: The value of the key in the dictionary.
"""
def getMonthName(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return months[month]

"""
It prints the name of the month centered in a 27 character wide field

:param month: The month to print
"""
def printMonth(month):
    monthName = getMonthName(month)
    print(" "*int((27-len(monthName))/2) + monthName, end="\n\n")

"""
It prints the calendar for the given month, with the given day highlighted.

:param startingDayOfYear: The day of the week that the first day of the year falls on
:param month: the month you want to display
:param dayFromMonth: the day of the month you want to highlight
"""
def displayCalendar(startingDayOfYear, month, dayFromMonth):
    nonMonthDays = startingDayOfYear-1
    nextMonthBeginningDay = nonMonthDays+1
    daysInMonth = 0

    print("SUN MON TUE WED THU FRI SAT")

    for mm in range(1, month+1):    
        daysInMonth = getMonthDays(mm)
        
        if(mm == month):
            print((" "*4)*nonMonthDays, end="")
            for day in range(1, daysInMonth + 1):
                nonMonthDays += 1
                if(nonMonthDays%7 == 0): 
                    if(day == dayFromMonth): print(" " * (3-len(str(day))) + "*" + str(day))
                    else: print(" " * (3-len(str(day))) + str(day))
                else: 
                    if(day == dayFromMonth): print(" " * (3-len("*" + str(day))) + "*" + str(day), end=" ")
                    else: print(" " * (3-len(str(day))) + str(day), end=" ")
                        
        nonMonthDays = getNonMonthDays(daysInMonth, nextMonthBeginningDay)
        nextMonthBeginningDay = nonMonthDays + 1

"""
If the month is April, June, September, or November, return 30. If the month is February, return 28.
Otherwise, return 31.

:param month: The month you want to get the days for
:return: The number of days in the month.
"""
def getMonthDays(month):
    if(month == 4 or month == 6 or month == 9 or month == 11): return 30
    elif(month == 2): return 28
    else: return 31

"""
If the month has 31 days, then the number of non-month da month's bys is the nexteginning day plus
2, unless that's greater than 7, in which case it's the remainder of that plus 7. 
If the month has 30 days, then the number of non-month days is the next month's beginning day plus
1, unless that's greater than 7, in which case it's the remainder of that plus 7. 
If the month has 28 days, then the number of non-month days is the next month's beginning day minus
1, unless that's less than 0, in which case it's the remainder of that plus 7.

:param daysInMonth: The number of days in the current month
:param nextMonthBeginningDay: The day of the week that the next month begins on
:return: The number of days in the month.
"""
def getNonMonthDays(daysInMonth, nextMonthBeginningDay):
    
    if(daysInMonth == 31):
        if(nextMonthBeginningDay + 2 > 7): return (nextMonthBeginningDay + 2) % 7
        elif(nextMonthBeginningDay + 2 == 7): return 0
        else: return nextMonthBeginningDay + 2
    elif(daysInMonth == 30):
        if(nextMonthBeginningDay + 1 > 7): return 1
        elif(nextMonthBeginningDay + 1 == 7): return 0
        else: return nextMonthBeginningDay + 1
    else: return nextMonthBeginningDay - 1


startProgram()