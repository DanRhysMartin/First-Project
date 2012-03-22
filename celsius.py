while 1: 
    print "For Fahrenheit to Celsius, Press 1. For Celsius To Fahrenheit, Press 2."
    x = raw_input("1 or 2: ")
    if x == "1":
        F = input("Fahrenheit: ")
        C = (F - 32)*5/9
        print C
    elif x == "2":
        C = input("Celsius: ")
        F = C*9/5 + 32
        print F 
