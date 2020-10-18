# Print out numbers from 1 to 100 (including 100).
# But, instead of printing number 3, print "Fizz"
# Instead of printing number of 5, print "Buzz"
# Instead of printing number 3 and 5, print "FizzBuzz".

for numbers in range (1, 101):    
    if numbers == 3:
        print("Fizz")
    elif numbers == 5:
        print("Buzz")
    elif numbers == 35 and numbers == 53:
        print("Fizz Buzz") 
    else:
        print(numbers)
