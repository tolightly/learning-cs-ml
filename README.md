# learning-cs-ml
A learning repository: implementations from SICP, math, and ML basics.

## How to run
python sicp/<file>.py  (no output means all asserts passed)

## Contents
| File | What it checks | Notes |
|---|---|---|
| `sicp/sicp_Ch1_in_python.py` | Newton's method square root: recursive and iterative versions, asserts including x = 0 | [notes](notes/sicp_1_1_7.md) |
| `sicp/sicp_Ch1_in_Racket.rkt` | The same procedure in Racket (no asserts yet) | |

## What I found out
- SICP 1.1.7: the relative stopping test never succeeds when the root is 0, because the ratio stays constant. Details: [notes/sicp_1_1_7.md](notes/sicp_1_1_7.md)