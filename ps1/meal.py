def main():
    message = input("What time is it? ")
    time = convert(message)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 15:
        print("lunch time")
    elif time >= 17 and time <= 20:
        print("dinner time")
def convert(message):
    h, m = message.split(":")
    m1 = float(m) / 60
    return float(h) + m1