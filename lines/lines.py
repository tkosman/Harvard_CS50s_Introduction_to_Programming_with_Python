import sys

if len(sys.argv) < 2:
    sys.exit("Too few comand-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many comand-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")


counter = 0

try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[1]) as file:
    for line in file:
        if not line.isspace() and not line.strip().startswith("#"):
            counter += 1

file.close()
print(counter)


