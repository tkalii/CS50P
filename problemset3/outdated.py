# month-day-year order to year month day order
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    #ask user input 
    date = input("Date in MDY : ")
    try:
        month, day, year = date.split("/" or " ")
        #checking the validity of month and day
        if(int(month) >= 1 and int(month) <= 12) and (int(day) <= 31 and int(day) >= 1):
            break
    except:
        try:
            old_month, old_day, year = date.split(" ")
            for i in range(len(months)):
                if old_month == months[i]:
                    month =  i + 1
            day = old_day.replace(",", "")
            #checking the validity of month and day
            if(int(month) >= 1 and int(month) <= 12) and (int(day) <= 31 and int(day) >= 1):
                break
        except:
            #go to next line 
            print()
            pass
print(f"{year}-{int(month):02}-{int(day):02}")