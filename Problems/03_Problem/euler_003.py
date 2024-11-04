import math

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: Number to check if is prime

    Returns:
        bool: True if number is prime, False otherwise
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n: int) -> int:
    """
    Find the largest prime factor of a number.

    Args:
        n: Number to find its largest prime factor

    Returns:
        int: The largest prime factor
    """
    for i in range(int(math.sqrt(n)) + 1, 2, -1):
        if is_prime(i) and n % i == 0:
            return i


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))