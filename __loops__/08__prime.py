import math
input_number = int(input("Enter the number: "))
is_prime = True

if input_number>1:
    for i in range(2,int(math.sqrt(input_number))):
        if( input_number % i )== 0:
            is_prime = False
if is_prime:
    print("The number is prime")
else:print("Number is not prime")