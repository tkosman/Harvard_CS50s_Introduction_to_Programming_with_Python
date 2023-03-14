def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def dot_one(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    return True

def dot_three(s):
    been_letter = False
    for letter in s:
        if been_letter == False and letter.isnumeric():
            been_letter = True
            if letter == "0":
                return False
        if been_letter and letter.isalpha():
            return False
    return True

def dot_four(s):
    for letter in s:
        if not letter.isalpha() and not letter.isnumeric():
            return False
    return True


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if dot_one(s) and dot_three(s) and dot_four(s):
        return True
    return False

main()