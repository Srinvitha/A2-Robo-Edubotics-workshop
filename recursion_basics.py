# recursion_basics.py

def factorial(n):
    if n <= 1:  # base case
        return 1

    return n * factorial(n - 1)  # recursive case

print(factorial(5))

def countdown(n):
    if n <= 0:
        print("Liftoff!")
        return

    print(n)
    countdown(n - 1)

countdown(3)

def sum_list(numbers):
    if not numbers:  # base case: empty list
        return 0

    return numbers[0] + sum_list(numbers[1:])

print(sum_list([4, 8, 15, 16, 23]))
