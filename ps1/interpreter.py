expression = input("Expression:")
x, y, z = expression.split(" ")
x1 = float(x)
z1 = float(z)
if y == "+":
    answer = z1 + x1
if y == "*":
    answer = z1 * x1
if y == "-":
    answer = z1 - x1
if y == "/":
    answer = z1 / x1
print(round(answer, 1))