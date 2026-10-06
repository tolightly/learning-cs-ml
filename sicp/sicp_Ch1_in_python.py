# region Square root procedure - LISP-like structure (SICP 1.1.7)
"""Square root via Newton's method (SICP 1.1.7): a recursive LISP-like
implementation and an iterative Python-like one, checked with asserts."""
tolerance = 1e-6

def sqrt_newton_sicp_like(x):
    """Return the square root of x."""
    assert x >= 0, "Cannot compute square root of negative number."
    # Check for x == 0, because in this case loop never stops
    if x == 0:
        return 0
    def average(a, b):
        """Return the arithmetic mean of a and b."""
        return (a + b) / 2

    def improve(guess, x):
        """Improve guess using Newton's method"""
        return average(guess, (x / guess))

    def is_good_enough(guess, previous_guess):
        """Return True when the relative change between successive guesses is below tolerance."""
        # The absolute error is unsuitable for very large and very small values; use the relative change instead.
        return (abs(guess - previous_guess)) / guess < tolerance
    
    def sqrt_iter(guess, previous_guess, x):
        """Recursively improve guess until it is accurate enough.

        Parameters:
            x: radicand, the number whose square root is sought.
            guess: current candidate for the square root of x.
            previous_guess: guess from the previous iteration, used for the stopping test.

        If the guess is accurate enough, return it as the square root of x.
        Otherwise call sqrt_iter again with an improved guess."""
        if is_good_enough (guess, previous_guess):
            return guess
        else:
            return sqrt_iter(improve(guess, x), guess, x)
    
    return sqrt_iter(1.0, 0.0, x)
assert abs(sqrt_newton_sicp_like(0.0) - 0.0) < tolerance # Assert in absolute change causes divide by 0
assert abs(sqrt_newton_sicp_like(4.0) - 2.0) / 2.0 < tolerance
assert abs(sqrt_newton_sicp_like(100.0) - 10.0) / 10.0 < tolerance
assert abs(sqrt_newton_sicp_like(1e-14) - 1e-7) / 1e-7 < tolerance
assert abs(sqrt_newton_sicp_like(1e-12) - 1e-6) / 1e-6 < tolerance
# endregion

#region Square Root procedure - Python-like structure (SICP 1.1.7)
def sqrt_newton(x):
    """Return the square root of x."""
    assert x >= 0, "Cannot compute square root of negative number."

    # guess: current estimate of the square root of x.
    guess = 1.0
    # previous_guess: guess from the previous iteration, for the stopping test.
    previous_guess = 0.0
    # Check for x == 0, because it implies divide by zero error
    if x == 0:
        return 0
    # Stopping test: relative difference between guess and previous_guess.
    # When successive approximations barely change, the root is accurate enough.
    while abs(guess - previous_guess) / guess >= tolerance:
        previous_guess = guess # save guess for the next iteration
        guess = (guess + (x / guess)) / 2 # improve guess with Newton's method
    return guess

assert abs(sqrt_newton(0.0) - 0.0) < tolerance      
assert abs(sqrt_newton(4.0) - 2.0) / 2.0 < tolerance
assert abs(sqrt_newton(100.0) - 10.0) / 10.0 < tolerance
assert abs(sqrt_newton(1e-14) - 1e-7) / 1e-7 < tolerance
assert abs(sqrt_newton(1e-12) - 1e-6) / 1e-6 < tolerance
# endregion
