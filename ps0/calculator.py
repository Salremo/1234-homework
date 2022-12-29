def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    check = d.replace("$","")
    return float(check)


def percent_to_float(p):
    tip =  p.replace("%","")
    tip_converted = float(tip) / 100
    return(tip_converted)


main()