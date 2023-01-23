while True:
    try:
        x = int(input("what's x? "))
        sign = input("input an arithemtic sign ")
        y = int(input("what's y? "))
    except ValueError:
        print("wrong input in value")
    else:
        break
if sign == "+":
    print("answer:",(x+y))
elif sign == "-":
    print("answer:",(x-y))
elif sign == "*":
    print("answer:",(x*y))
elif sign =="/":
    print("answer:",(x/y))
else:
    print("wrong input in sign")

