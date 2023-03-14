def main():
    current = input("What time is it? ")
    if 7 <= convert(current) <= 8:
        print("breakfast time")
    elif 12 <= convert(current) <= 13:
        print("lunch time")
    elif 18 <= convert(current) <= 19:
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":")
    general = float(hour) + float(minutes)/60
    return general

if __name__ ==  "__main__":
    main()