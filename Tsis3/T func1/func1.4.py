def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

input_numbers = input("Input: ")
numbers_list = [int(x) for x in input_numbers.split()]
prime_numbers = filter_prime(numbers_list)
print("Output:", prime_numbers)
