tekst = input("Input: ")
not_allowed = ["A","a", "E", "e", "I", "i", "O", "o", "U", "u"]

for letter in tekst:
    if not letter in not_allowed:
        print(letter, sep="", end="")

print("")