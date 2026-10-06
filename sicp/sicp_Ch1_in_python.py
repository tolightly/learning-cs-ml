# region Square root procedure - LISP-like structure (SICP 1.1.7)
tolerance = 1e-6

def sqrt_newton_sicp_like(x):
    """Return the square root of x."""
    assert x >= 0, "Cannot compute square root of negative number."
    
    def average(a, b):
        """Takes two numbers and returns arithmetic mean of them"""
        return (a + b) / 2

    def improve(guess, x):
        """Improve guess using Newton's method"""
        return average(guess, (x / guess))

    def is_good_enough(guess, previous_guess):
        """Predicate that verifies the accuracy of an guess based on it's magnitude of change"""
        # The absolute error value is unsuitable for handling very large and very small values; the relative value must be used instead.
        return (abs(guess - previous_guess)) / guess < tolerance
    
    def sqrt_iter(guess, previous_guess, x):
        """Helper procedure that recursively improves guess until it becomes sufficiently accurate
        Formal parameters:
            x: radicand - значення, квадратний корінь якого ми шукаємо.
            guess: значення, щодо якого ми припускаємо, що воно є квадратним коренем x і це твердження слід перевірити.
            previous-guess: значення guess з попередньої ітерації для перевірки умови зупинки.
    Якщо наше припущення достатньо точне, то ми повертаємо це припущення як результат - квадратний корінь x.
    Якщо припущення неточне, то рекурсивно викликаємо всю процедуру знову, але передаємо покращене припущення."""
        if x == 0:
            return 0 
        elif is_good_enough (guess, previous_guess):
            return guess
        else:
            return sqrt_iter(improve(guess, x), guess, x)
    
    return sqrt_iter(1.0, 0.0, x)
assert abs(sqrt_newton_sicp_like(0.0) - 0.0) < tolerance
assert abs(sqrt_newton_sicp_like(4.0) - 2.0) < tolerance
assert abs(sqrt_newton_sicp_like(100.0) - 10.0) < tolerance
# endregion

#region Square Root procedure - Python-like structure (SICP 1.1.7)
def sqrt_newton(x):
    """Return the square root of x."""
    assert x >= 0, "Cannot compute square root of negative number."

    # We use the guess to estimate the value that is the root of x.
    guess = 1.0
    # We use the previous_guess to saving the value of the guess from previous iteration.
    previous_guess = 0.0
    # Guard: is_good_enough: relative difference between guess and previous_guess. 
    # When the difference between successive approximations changes very little during iteration, we have found a sufficiently accurate value of the root.
    if x == 0:
        return 0
    
    while abs(guess - previous_guess) / guess >= tolerance:
        previous_guess = guess # Saving guess for next iteration
        guess = (guess + (x / guess)) / 2 # Improving guess based on Newnon's method
    return guess

assert abs(sqrt_newton(0.0) - 0.0) < tolerance      
assert abs(sqrt_newton(4.0) - 2.0) < tolerance
assert abs(sqrt_newton(100.0) - 10.0) < tolerance
# endregion
