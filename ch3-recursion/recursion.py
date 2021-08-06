# implementing factorial calc using recursion
def factorial(number):
    if number < 2:
        return 1
    return number * factorial(number-1)
