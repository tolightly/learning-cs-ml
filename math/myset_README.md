# myset.py: finite sets from scratch

A small learning project: finite sets implemented with only Python lists
and plain functions (no classes, no built-in `set` in the implementation),
following Hammack, *Book of Proof*, chapter 1. The built-in `set` and
`frozenset` appear only in the test code, as a reference.

## Representation

- A set is a `list` without duplicates. The empty set is `[]`; the set
  containing the empty set is `[[]]`.
- A nested list is treated as a set: `[1, 2]` and `[2, 1]` are the same
  element of an outer set.
- Ordered pairs are tuples, built with `make_pair`. This is a temporary
  deviation (a list cannot tell a pair from a set); I plan to revisit it
  after SICP section 2.4.2 on tagged data.
- `myset(lst)` is the constructor: it removes duplicates. The "no duplicates"
  invariant is established only here. The operations trust their input and do
  not normalize it.

## Implemented

`myset`, `cardinality`, `is_member`, `no_dubs`, `is_set`, `is_subset`,
`is_equal_sets`, `cartesian_product`, `union_sets`, `intersection_sets`,
`diffence_sets` (sic), `complement_set`, `powerset`.

## How to run

    python myset.py

Python [version]. No output means every assertion passed.

## What the assertions check

- Operation results are compared with hand-written expected values at the
  level of sets, not lists: a test helper (`assert_same_set`) converts nested
  lists to `frozenset` and also fails if the result contains duplicates.
  Comparing lists with `==` would depend on element order.
- Algebraic laws: commutativity and idempotence of union and intersection,
  `(A \ B) ∩ B = ∅`, `U \ (U \ A) = A`, and the `ValueError` branch of
  `complement_set`.
- `powerset`: [after you add them: `len(result) == 2**len(A)`, every element
  is a subset of `A`, no duplicates in the result, the input is not modified].

## Known limits

- Inputs that contain duplicates (including nested lists with duplicates) are
  outside the contract. `is_equal_sets` silently normalizes them with `myset`,
  so such inputs may hide mistakes instead of failing.
- Not tested: that operations leave their inputs unchanged; aliasing for
  nested inputs (`powerset` may reuse the same inner list in several
  subsets).
- `is_member` on nested lists is recursive and slow; no attention to
  performance so far.

## What I found out
- Lists compare by order, so `[2, 3] == [3, 2]` is `False`; membership of
  nested sets needs set equality, not `==`.
- A `TypeError` in `myset` traced to a nested list with duplicates (`[3, 3]`):
  an invalid input was allowed to exist, and the fix was a rule about where
  the invariant is established.