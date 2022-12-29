CamelCase = input("CamelCase:")
print("SnakeCase: ", end="")
for message in CamelCase:
    if message.isupper():
        print("_" + message.lower(), end="")
    else:
        print(message, end="")
print()