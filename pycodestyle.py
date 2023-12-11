def sum_even_fibonacci(limit):
    """
    Calculate the sum of even Fibonacci numbers below the given limit.

    Parameters:
    - limit (int): The upper limit for Fibonacci numbers.

    Returns:
    - int: The sum of even Fibonacci numbers below the limit.
    """
    a, b = 1, 2
    even_sum = 0

    while a < limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum


# Example usage:
limit = 4000000
result = sum_even_fibonacci(limit)
print(f"The sum of even Fibonacci numbers below {limit} is: {result}")

