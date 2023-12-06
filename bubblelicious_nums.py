def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any other number, it's not prime

    return True  # If no factors were found, the number is prime



bubble_num = [num * 16 + 11 for num in range(100000) if num * 16 + 11 <= boundary[-1] and is_prime(num * 16 + 11)]
len(bubble_num)
