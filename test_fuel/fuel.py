def main():
    print(convert("2/3"))

def convert(fraction):
    if type(fraction) is not str:
        raise ValueError
    X, Y = fraction.split("/")

    X = int(X)
    Y = int(Y)

    if Y == 0:
        raise ZeroDivisionError

    if X > Y:
        raise ValueError

    return round(X / Y * 100)

def gauge(percentage):
    if type(percentage) is not int:
        raise ValueError
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()