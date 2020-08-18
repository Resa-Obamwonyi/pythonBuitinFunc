def fizz_buzz(n):
  if n >= 1:
    newlist = [i for i in range(n+1) if i>=1]
    newstr = ""
    for x in newlist:
      if x == 1: newstr+=str(x)
      elif x%3 == 0 and x%5 == 0: newstr+="\n"+"FizzBuzz"
      elif x%5 == 0: newstr+= "\n"+"Buzz"
      elif x%3 == 0: newstr+= "\n"+"Fizz"
      else: newstr+= "\n"+ str(x)
    return repr(newstr)
  else:
    return "Invalid"


print(fizz_buzz(20))