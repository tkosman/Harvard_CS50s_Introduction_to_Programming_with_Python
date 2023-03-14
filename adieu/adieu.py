import inflect

p = inflect.engine()

name_list = []

while True:
    try:
        name = input("Input: ")
    except EOFError:
        print("Adieu, adieu, to " + p.join(name_list))
        break

    name_list.append(name)