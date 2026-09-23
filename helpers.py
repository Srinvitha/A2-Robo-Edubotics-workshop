# helpers.py
# a module: just function definitions, nothing runs on its own

def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False

    return True

def is_palindrome(word):
    cleaned = word.lower()
    return cleaned == cleaned[::-1]
