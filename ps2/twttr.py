answer = input("Input: ")
print("Output: ", end="")
for message in answer:
    if not message.lower() in ['a','i','e','u','o']:
        print(message, end="")
print()