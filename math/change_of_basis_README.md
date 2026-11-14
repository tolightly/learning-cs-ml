# change_of_basis

A learning script: coordinates of a vector in a new basis (2D, no NumPy).
Main function: `coords(v, b1, b2)`.

## Usage
`python change_of_basis.py`. The output is empty if all asserts pass.

## What the asserts check
- orientation, `p=0`, `r=0`, negative coordinate
- `ValueError` for dependent and nearly dependent vectors
- comparison of lists containing numbers near zero

## What I found out
Before checking whether a value equals zero (e.g. `p == 0`) in order to raise an error or to claim that no solution exists, check whether that condition really follows from the nature of the problem, or whether it is merely a consequence of the chosen computation path (derivation).

## Limitations
The `1e-9` tolerance for `det` is absolute: it does not adapt to the scale of the numbers.