# bin(x)- Converts an integer into binary
# hex(x) - Converts an integer into hexadecimal

def binaryConvert(num):
    return bin(num)


print(binaryConvert(27))
print(binaryConvert(298))


# enumerate(object)- returns an enumerate object

def enumerateObj(lst):
    return list(enumerate(lst))


print(enumerateObj(["Fish", "Eggs", "Milk", "Tomatoes", "Cereal"]))