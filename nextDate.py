def nextDate(day,month,year):
    newDay = day
    newMonth = month
    newYear = year
    switcher = {1 : 31,2 : 28,3 : 31,4 : 30,5 : 31,6 : 30,7 : 30,8 : 31,9 : 30,10 : 31,11 : 30,12 : 31}
    if year % 400 == 0:
        switcher[2] = 29
    if day > switcher[month]:
        print("Invalid date")
        return
    if day == switcher[month]:
        newDay = 1
        if month == 12:
            newMonth = 1
            if year == 2014:
                print("year exceeded")
                return
            else:
                newYear = year + 1
        else:
            newMonth = month + 1
    else:
        newDay = day + 1
    print(str(newDay) + '-' + str(newMonth) + '-' + str(newYear))
    return

if __name__ == "__main__":
    while True:
        day = int(input("Enter day: "))
        if day < 1 or day > 31:
            print("Invalid day")
            continue
        month = int(input("Enter month: "))
        if month < 1 or month > 12:
            print("Invalid month")
            continue
        year = int(input("Enter year: "))    
        if year < 1812 or year > 2014:
            print("Invalid year")
            continue    
        nextDate(day,month,year)

