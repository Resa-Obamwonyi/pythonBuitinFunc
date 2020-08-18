# raising an error
#raise NameError(" Error loading name")


# raising an exception and handling exceptions

def exceptionTest(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("Hey, you cannot divide by zero")
    else:
        print("Hey, you had no exceptions")

print(exceptionTest(3,0))