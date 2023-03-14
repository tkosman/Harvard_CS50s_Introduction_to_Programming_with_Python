camel_case = input("camelCase: ")
print("snake_case: ", end="")
for letter in camel_case:
    if letter.isupper() == True:
        print("_" + letter.lower(), sep="", end="")
    else:
        print(letter, sep="", end="")

print("")