numlist = list(range(1,101))
for x in numlist:
    if x%3==0 and x%5==0:
        x = "FizzBuzz"
        print (x)
    elif x%3==0:
        x = "Fizz"
        print (x)
    elif x%5==0:
        x = "Buzz"
        print (x)
    else:
        print(x)
