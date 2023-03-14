import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)

        check = 0
        while True:
            print(f"{X} + {Y} = ", end="")
            result = int(input())
            if result == X + Y:
                score += 1
                break
            else:
                print("EEE")
                check += 1
                if check == 3:
                    print(X + Y)
                    break




    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level < 1:
                raise ValueError
            return level
        except ValueError:
            pass
        except EOFError:
            print("")
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()