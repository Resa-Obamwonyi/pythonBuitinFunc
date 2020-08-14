def divisors(integer):
    newlist = [x for x in range(2, integer) if integer % x == 0]
    if len(newlist) == 0:
        return str(integer) + " is prime"
    else:
        return newlist


print(divisors(12))
print(divisors(23))
print(divisors(15))
print(divisors(125))