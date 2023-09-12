def is_happy(n):
    def sum_of_squared_digits(num):
        # This function calculates the sum of the squares of the digits of num.
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total

    seen = set()  # To keep track of seen numbers to detect cycles.
    
    while n != 1:
        if n in seen:
            return False  # We detected a cycle that doesn't include 1, so it's not a happy number.
        seen.add(n)
        n = sum_of_squared_digits(n)

    return True  # If we reach 1, it's a happy number.


# Example Usage
print(is_happy(19))  # Output: True

print(is_happy(2))  # Output: False

print(is_happy(7))  # Output: True