def main():
    time = input("What is the time:")
    eating_time = convert(time)
    if (eating_time >= 7 and eating_time <= 8):
        print("Breakfast time!")
    elif (eating_time >= 12 and eating_time <= 13):
        print("Lunch time!")
    elif (eating_time >= 18 and eating_time <= 19):
        print("Dinner time!")


def convert(time):
    hours, mins = time.split(":")
    hours = float(hours) + (float(mins) / 60)
    return hours


if __name__ == "__main__":
    main()