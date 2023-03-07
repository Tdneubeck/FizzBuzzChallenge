#create list one through 100 and naming it numlist
numlist = list(range(1,101))
#going through numlist one number ata time and checking if it needs to be changed
for x in numlist:
    #if the number has a remainer of zero (divisble by) when divided by 3 and 5, change the number to the word FizzBuzz
    if x%3==0 and x%5==0:
        x = "FizzBuzz"
    #if the number has a remainer of zero (divisble by) when divided by 3 but not divisible by 5, change the number to the word Fizz
    elif x%3==0:
        x = "Fizz"
    #if the number has a remainer of zero (divisble by) when divided by 5 but not divisible by 3, change the number to the word Buzz
    elif x%5==0:
        x = "Buzz"
    #If the number is not divisble by 3 and or 5 leave the number as is.
    else:
        x=x
    #print the new list
    print (x)
