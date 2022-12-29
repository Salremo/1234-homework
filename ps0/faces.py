def main():
    message = input()
    end = faces(message)
    print(end)
def faces(message):
    message1 = message.replace(":)","🙂")
    message2 = message1.replace(":(","🙁")
    return message2
main()



