numlist = list(range(1,101))
for x in numlist:
    if x%3==0 and x%5==0:
        x = "FizzBuzz"
    elif x%3==0:
        x = "Fizz"
    elif x%5==0:
        x = "Buzz"
    else:
        x=x
    print (x)
