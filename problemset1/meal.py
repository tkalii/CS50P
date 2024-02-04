def main():
    toeat = input("What is the time? ")
    time = convert(toeat)

    if (time >= 7 and time <=8):
        print("Breakfast Time")
    elif (time >= 12 and time <=13):
        print("Lunch Time")
    elif (time >= 18 and time <=19):
        print("Dinner Time")
    else:
        pass

def convert(time):
    hour, minute = time.split(":")
    minute = float(minute) / 60
    hour = float(hour) + minute
    return hour

if __name__ == "__main__":
    main()