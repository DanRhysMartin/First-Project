""" 
    The benefit of Python is that code is readable. 
    Really readable. 
    while 1: isn't really readable. 
    Use while True: instead
"""

while 1:
    
    print "For Fahrenheit to Celsius, Press 1. For Celsius To Fahrenheit, Press 2."
    
    # You should really use names that tell you what a variable does. 
    # What do you think x does? Wouldn't "choice" be a better name?
    x = raw_input("1 or 2: ")
    
    if x == "1":
        # Never, ever use input in Python 2.x unless you know what you're doing. 
        # It has nasty side effects.
        # Also, try and use more spaces - it gives code a flow, like paragraphs.
        # Captials should only be used for constant variable names 
        # - things that will never, ever change, and will always be the same no matter 
        # how many times you run it
        F = input("Fahrenheit: ")
        
        # Really, you should use spaces between operations - ((F - 32) * 5) / 9 is clearer.
        C = (F - 32)*5/9
        
        print C
        
    elif x == "2":
        C = input("Celsius: ")
        F = C*9/5 + 32
        print F 
