def queryInput():
    print("\n============================================\n")
    startingDayOfYear = int(input("What day of the week the year begins (1 - Sun, 2 - Mon, ..., 7 - Sat): "))
    while(not(startingDayOfYear >= 1 and startingDayOfYear <= 7)):
        print("Day of week is invalid! Please try again.")
        print("\n============================================\n")
        startingDayOfYear = int(input("What day of the week the year begins (1 - Sun, 2 - Mon, ..., 7 - Sat): "))
    
    month = int(input("Choose a month (1 - Jan, 2 - Feb, ..., 12 - Dec): "))
    while(not(month >= 1 and month <= 12)):
        print("Month is invalid! There are 12 month, please try again.")
        print("\n============================================\n")
        month = int(input("Choose a month (1 - Jan, 2 - Feb, ..., 12 - Dec): "))

    dayFromMonth = int(input("Choose a day from the given month: "))
    while(not(dayFromMonth <= getMonthDays(month))):
        print(getMonthName(month) + " only have " + str(getMonthDays(month)) + " days! Please try again.")
        print("\n============================================\n")
        dayFromMonth = int(input("Choose a day from the given month: "))
    print("\n============================================\n")

    generateCalendar(startingDayOfYear, month, dayFromMonth)

def generateCalendar(startingDayOfYear, month, dayFromMonth):
    printMonth(month)
    displayCalendar(startingDayOfYear, month, dayFromMonth)
    print("\n\n============================================\n")

def getMonthName(month):
    if(month == 1): return "January"
    elif(month == 2): return "February"
    elif(month == 3): return "March"
    elif(month == 4): return "April"
    elif(month == 5): return "May"
    elif(month == 6): return "June"
    elif(month == 7): return "July"
    elif(month == 8): return "August"
    elif(month == 9): return "September"
    elif(month == 11): return "November"
    elif(month == 12): return "December"

def printMonth(month):
    monthName = getMonthName(month)
    print(" "*int((27-len(monthName))/2) + monthName, end="\n\n")

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

def getMonthDays(month):
    if(month == 4 or month == 6 or month == 9 or month == 11): return 30
    elif(month == 2): return 28
    else: return 31

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

queryInput()