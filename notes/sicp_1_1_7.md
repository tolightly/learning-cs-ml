## What I found out
### SICP 1.1.7 - Square root, Newton's method
#### return
After SICP I find it hard to readjust to `return` in Python: I keep forgetting that a function has to hand back a value through `return`. In Lisp there is no such keyword, and no need for it, as far as I know.
After some digging I learned the reason: imperative languages work with `statements` - instructions to the interpreter to perform actions. Separate from them there are `values`. A function body is just a sequence of statements and does not produce a value by itself, so I have to say explicitly which value to hand back. That is what `return` does (a function without `return` gives back `None`).
In Scheme every expression has a value, so the value of the last expression in a procedure body is the result automatically.
This is a difference in language design and paradigm.

#### Recursion is inefficient in Python
I can implement the recursive procedure `sqrt_newton_sicp_like` in Python and it works, calling itself. But, as it turned out, it is less efficient than its Scheme counterpart.
Tail recursion is efficient in Scheme because the interpreter runs it as an iterative process: only one "snapshot" of the procedure state exists in the stack and memory, and each next call with updated arguments replaces the previous one.
Python does not perform tail call optimisation, so even when there are no deferred operations the interpreter keeps a frame for every call. When the recursion limit is reached (1000 by default, see `sys.getrecursionlimit()`), Python raises `RecursionError`.

#### Why Lisp does not need loops
It was interesting to compare loops and recursive procedures in Scheme and Python.
Scheme can do without dedicated loops because (my current understanding):
- everything is an expression with a value;
- the interpreter does tail call optimisation, so tail recursion runs as an iterative process;
- there are built-in higher-order functions for processing lists.

Imperative languages have `while` and `for` loops because (my hypothesis, to verify):
- they follow the von Neumann architecture: a computer executes instructions in sequence and writes the results to memory cells, so loops describe low-level machine behaviour. `while` and `for` closely resemble `JUMP` instructions, which makes them very efficient;
- this fits the spirit of imperative languages, which is state mutation: loops change local variables as they run.

#### Absolute and relative error (delta)
The absolute error (difference, delta) does not depend on the magnitude of the numbers being compared, so a fixed threshold can misbehave for very large or very small values:
$|guess - \text{prev\_guess}| < tolerance$ (first version of `is_good_enough` in `sqrt_newton_sicp_like`).
Absolute error doesn't work when `tolerance` is greater than answer (`guess`). 
For example: 
assert abs(sqrt_newton(1e-14) - 1e-07) < 1e-6
abs(9.57167e-07 - 1e-07) < 1e-6 is True, although the result is incorrect

The relative error depends on the magnitude of the compared values, so it handles very large and very small values better. To get the relative value I divided the difference by one of the values:
$|guess - \text{prev\_guess}| / guess < tolerance$ (second version of `is_good_enough` in `sqrt_newton_sicp_like`).

Relative error = absolute error / guess.

##### How the relative error breaks down at x == 0 in `sqrt_newton`
Consider the stopping test `(abs(guess - previous_guess)) / guess < tolerance` when `x == 0`.
Initial state: `(abs(1.0 - 0.0)) / 1.0 = 1`.
For the following iterations (here `guess` is the value before the update):

```
abs((guess + (0 / guess)) / 2 - guess) / ((guess + (0 / guess)) / 2)
= abs(guess / 2 - guess) / (guess / 2)
= (guess / 2) / (guess / 2) = 1
```

So during the loop with `x == 0` the value of `(abs(guess - previous_guess)) / guess` does not change and always equals 1. As a result, the stopping condition never fires.
The reason: `abs(guess - previous_guess)` is the absolute change, and `abs(guess - previous_guess) / guess` is the relative change, so relative change = absolute change / `guess`. When `x == 0`, both the absolute change and `guess` itself tend to 0 at the same rate: each new guess is exactly half of the previous one, so their ratio is always exactly 1. The relative change measures the change in units of the value itself, so when the value tends to 0, the scale disappears and the stopping condition never fires.