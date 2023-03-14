import math

while True:
    try:
        X, Y = input("Fraction: ").split("/")
        fract = round(int(X) / int(Y) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if fract > 100:
            pass
        elif fract >= 99:
            print("F")
            break
        elif fract <= 1:
            print("E")
            break
        else:
            print(fract, "%", sep="", end="")
            break


