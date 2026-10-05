# region Square root procedure - LISP-like structure (SICP 1.1.7)
tolerance = 1e-6

def sqrt_newton(x):
    """Return the square root of x."""
    assert x >= 0, "Cannot compute square root of negative number."
    
    return sqrt_iter(1.0, 0.0, x)

def sqrt_iter(guess, previous_guess, x):
    if is_good_enough (guess, previous_guess):
        print('Result is: ', guess)
        return guess
    else:
        print('guess is', guess, 'x is', x)
        return sqrt_iter(improve(guess, x), guess, x)

def improve(guess, x):
    return average(guess, (x / guess))

def average(a, b):
    return (a + b) / 2

def is_good_enough(guess, previous_guess):
    return (abs(guess - previous_guess)) / guess < tolerance

assert abs(sqrt_newton(4.0) - 2.0) < 1e-6
assert abs(sqrt_newton(100.0) - 10.0) < 1e-6
sqrt_newton(10000000000000)

# endregion

#region Square Root procedure - Python-like structure (SICP 1.1.7)

