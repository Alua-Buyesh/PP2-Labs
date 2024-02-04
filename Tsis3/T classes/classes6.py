def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        
    return True

arr=[11,3 ,4 ,67,55,9, 7, 99, 87, 53]

prime_numbers = list(filter(lambda x: is_prime(x), arr))
print(prime_numbers)