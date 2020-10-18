#to print the prime number of a given range of numbers
user_number = int(input("Enter the numbers upto which the prime numbers has to be identified: "))
for n in range(1, user_number):    
    if user_number % n == 0:
        print("It is not a prime number.")
    else:
        print("It is a prime number.")
