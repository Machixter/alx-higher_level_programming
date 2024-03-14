#!/usr/bin/python3
if __name__ == "__main__":
    """ print the difference, sum, product and quotient of 10 and 5 """
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    """ calculate the results """
    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)

    """ construct the output string """
    output = f"{a} + {b} = {addition}\n"
    output += f"{a} - {b} = {subtraction}\n"
    output += f"{a} * {b} = {multiplication}\n"
    output += f"{a} / {b} = {division}"

    """ print the output """
    print(output)

       #print("{} + {} = {}".format(a, b, add(a, b)))
       #print("{} - {} = {}".format(a, b, sub(a, b)))
       #print("{} * {} = {}".format(a, b, mul(a, b)))
       #print("{} / {} = {}".format(a, b, div(a, b)))
