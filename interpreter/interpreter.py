x, y, z = input("Expression: ").split()
x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

print(float(result))