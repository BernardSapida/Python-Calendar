print("\n============================================\n")
startingDayOfYear = int(input("What day of the week the year begins (1 - Sun, 2 - Mon, ..., 7 - Sat): "))
while(not(startingDayOfYear >= 1 and startingDayOfYear <= 7)):
    print("Day of week is invalid! Please try again.")
    print("\n============================================\n")
    startingDayOfYear = int(input("What day of the week the year begins (1 - Sun, 2 - Mon, ..., 7 - Sat): "))

month = int(input("Choose a month (1 - Jan, 2 - Feb, ..., 12 - Dec): "))
while(not(month >= 1 and month <= 12)):
    print("month is invalid! There are 12 month, please try again.")
    print("\n============================================\n")
    month = int(input("Choose a month (1 - Jan, 2 - Feb, ..., 12 - Dec): "))

dayFromMonth = int(input("Choose a day from the given month: "))
while(True):
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

    if(month == 4 or month == 6 or month == 9 or month == 11): daysInMonth = 30
    elif(month == 2): daysInMonth = 28
    else: daysInMonth = 31

    if(dayFromMonth <= daysInMonth and dayFromMonth > 0): break

    print("Invalid date! There is no " + months[month] + " " + str(dayFromMonth) + "!")
    print("\n============================================\n")
    dayFromMonth = int(input("Choose a day from the given month: "))
        
nonMonthDays = startingDayOfYear-1
nextMonthBeginningDay = nonMonthDays+1
daysInMonth = 0
monthName = ""

if(month == 1): monthName = "January"
elif(month == 2): monthName = "February"
elif(month == 3): monthName = "March"
elif(month == 4): monthName = "April"
elif(month == 5): monthName = "May"
elif(month == 6): monthName = "June"
elif(month == 7): monthName = "July"
elif(month == 8): monthName = "August"
elif(month == 9): monthName = "September"
elif(month == 11): monthName = "November"
elif(month == 12): monthName = "December"

print("\n============================================\n")
print(" "*int((27-len(monthName))/2)+ monthName, end="\n\n")

print("SUN MON TUE WED THU FRI SAT")
for mm in range(1, month+1):    
    if(mm == 4 or mm == 6 or mm == 9 or mm == 11): daysInMonth = 30
    elif(mm == 2): daysInMonth = 28
    else: daysInMonth = 31
    
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
                    
    if(daysInMonth == 31):
        if(nextMonthBeginningDay + 2 > 7): nonMonthDays = (nextMonthBeginningDay + 2) % 7
        elif(nextMonthBeginningDay + 2 == 7): nonMonthDays = 0
        else: nonMonthDays = nextMonthBeginningDay + 2
    elif(daysInMonth == 30):
        if(nextMonthBeginningDay + 1 > 7): nonMonthDays = 1
        elif(nextMonthBeginningDay + 1 == 7): nonMonthDays = 0
        else: nonMonthDays = nextMonthBeginningDay + 1
    else: nonMonthDays = nextMonthBeginningDay - 1
    nextMonthBeginningDay = nonMonthDays + 1

print("\n\n============================================\n")