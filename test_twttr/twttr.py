def main():
    print(shorten("AIOD"))


def shorten(word):
    not_allowed = ["A","a", "E", "e", "I", "i", "O", "o", "U", "u"]
    new_word = ""
    for letter in word:
        if not letter in not_allowed:
            new_word += letter
    return new_word


if __name__ == "__main__":
    main()