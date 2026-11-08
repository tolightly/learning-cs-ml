def myset(lst: list) -> list:
    i = 0
    i_max = cardinality(lst)
    result = []
    while i < i_max:
        if not is_member(lst[i], result):
            result.append(lst[i])
        i = i + 1
    return result
def make_pair(first, second) -> tuple:
    return (first, second)
def first(tuple: tuple):
    return tuple[0]
def second(tuple: tuple):
    return tuple[1]

def cardinality(set: list) -> int:
    return len(set)

def no_dubs(set: list) -> bool:
    i = 0
    i_max = cardinality(set)
    while i < i_max:
        if is_member(set[i], set[i+1:]):
            return False
        i = i + 1
    return True

def is_set(set: list) -> bool:
    if not no_dubs(set):
        return False
    return True

def is_member(element, set: list) -> bool:
    i = 0
    i_max = cardinality(set)
    while i < i_max:
        if isinstance(element, list) and isinstance(set[i], list):
            if is_equal_sets(element, set[i]):
                return True
        elif element == set[i]:
            return True
        i = i + 1
    return False

def is_subset(subset: list, set: list) -> bool:
    i = 0
    i_max = cardinality(subset)
    while i < i_max:
        if not is_member(subset[i], set):
            return False
        i = i + 1
    return True
    
def is_equal_sets(set1: list, set2: list) -> bool:
    if not is_set(set1):
       set1 = myset(set1) 
    if not is_set(set2):
        set2 = myset(set2)
    if is_subset(set1, set2) and is_subset(set2, set1):
        return True
    return False

def cartesian_product(set1: list, set2: list) -> list:
    i = 0
    i_max = cardinality(set1)
    j_max = cardinality(set2)
    result = []
    while i < i_max:
        j = 0
        while j < j_max:
            result.append(make_pair(set1[i], set2[j]))
            j = j + 1
        i = i + 1
    return result

def union_sets(set1: list, set2: list) -> list:
    i = 0
    j = 0
    i_max = cardinality(set1)
    j_max = cardinality(set2)
    result = []
    while i < i_max:
        result.append(set1[i])
        i = i + 1
    while j < j_max:
        result.append(set2[j])
        j = j + 1
    return myset(result)

def intersection_sets(set1: list, set2: list) -> list:
    i = 0
    i_max = cardinality(set1)
    result = []
    while i < i_max:
        if is_member(set1[i], set2):
            result.append(set1[i])
        i = i + 1
    return result

def difference_sets(set1: list, set2: list) -> list:
    i = 0
    i_max = cardinality(set1)
    result = []
    while i < i_max:
        if not is_member(set1[i], set2):
            result.append(set1[i])
        i = i + 1
    return result

def complement_set(set: list, universal: list) -> list:
    if not is_subset(set, universal):
            raise ValueError("Set must be a subset of universal")
    return difference_sets(universal, set)

def powerset(set: list) -> list:
    if cardinality(set) == 0:
        return [[]]
    rest = powerset(set[1:])
    return rest + list(map(lambda x: [set[0]] + x, rest))

# Helper function for testing
def _freeze_pair_component(value):
    if isinstance(value, list):
        return ("list", tuple(
            _freeze_pair_component(x) for x in value
        ))

    if isinstance(value, tuple):
        return ("tuple", tuple(
            _freeze_pair_component(x) for x in value
        ))

    return value


def _freeze_set_element(value):
    if isinstance(value, list):
        return _freeze_set(value)

    if isinstance(value, tuple):
        return ("tuple", tuple(
            _freeze_pair_component(x) for x in value
        ))

    return value


def _freeze_set(value):
    items = [_freeze_set_element(x) for x in value]
    frozen = frozenset(items)

    assert len(items) == len(frozen), (
        f"Duplicate elements found: {value!r}"
    )

    return frozen


def assert_same_set(actual, expected):
    assert _freeze_set(actual) == _freeze_set(expected), (
        f"Expected {expected!r}, got {actual!r}"
    )

# ============================================================
# 1. make_pair(), first(), second(), cardinality()
# ============================================================

assert make_pair(1, 2) == (1, 2)

assert first(make_pair(1, 2)) == 1
assert second(make_pair(1, 2)) == 2

assert cardinality([]) == 0
assert cardinality([1, 2, 3]) == 3


# ============================================================
# 2. myset()
# ============================================================

assert myset([]) == []

assert myset([1]) == [1]

assert myset([1, 2, 1, 3, 2]) == [1, 2, 3]

assert myset([1, 1, 1, 1]) == [1]

assert myset([[1, 2], [2, 1]]) == [[1, 2]]

assert myset([(1, 2), (2, 1)]) == [(1, 2), (2, 1)]

assert myset(myset([1, 2, 1, 3, 2])) == [1, 2, 3]


# ============================================================
# 3. no_dubs()
# ============================================================

assert no_dubs([])

assert no_dubs([1])

assert no_dubs([1, 2, 3])

assert not no_dubs([1, 2, 1])

assert not no_dubs([1, 1, 1])

assert not no_dubs([[], []])

assert not no_dubs([[2, 3], [3, 2]])

assert no_dubs([[2, 3], [2, [2, 3]]])

assert no_dubs([(1, 2), (2, 1)])


# ============================================================
# 4. is_set()
# ============================================================

assert is_set([])

assert is_set([1, 2, 3])

assert not is_set([1, 2, 1])

assert not is_set([[1, 2], [2, 1]])

assert is_set([(1, 2), (2, 1)])


# ============================================================
# 5. is_member()
# ============================================================

assert is_member(1, [1, 2, 3])

assert is_member(3, [1, 2, 3])

assert not is_member(4, [1, 2, 3])

assert not is_member(1, [])

assert not is_member([], [1, 2, 3])

assert is_member([], [[], 1, 2, 3])

assert is_member([1, 2], [[2, 1]])

assert not is_member([1, 2], [(1, 2)])

assert is_member([2, 3], [[3, 2], [1, [2, 1]]])

assert not is_member([2, 3], [[3, 1], [1, [2, 3]]])

assert is_member((1, 2), [(1, 2)])

assert not is_member((1, 2), [(2, 1)])


# ============================================================
# 6. is_subset()
# ============================================================

assert is_subset([], [])

assert is_subset([], [1, 2])

assert is_subset([1, 2, 3], [1, 2, 3])

assert is_subset([1, 2], [1, 2, 3])

assert not is_subset([1, 2, 3], [1, 2])

assert not is_subset([1, 4], [1, 2, 3])

assert not is_subset([[3, 4]], [2, 3, 4])

assert is_subset([[3, 4]], [2, [3, 4]])

assert is_subset([[1, 2]], [[2, 1], [3, 4]])

assert not is_subset(
    [make_pair(1, 2)],
    [make_pair(2, 1), make_pair(1, 1)]
)

assert is_subset(
    [make_pair(1, 2)],
    [make_pair(1, 2), make_pair(1, 1)]
)


# ============================================================
# 7. is_equal_sets()
# ============================================================

assert is_equal_sets([], [])

assert not is_equal_sets([], [[]])

assert is_equal_sets([1, 2], [1, 2])

assert is_equal_sets([1, 2, 3], [3, 2, 1])

assert not is_equal_sets([1, 2], [1, 2, 3])

assert not is_equal_sets([1, [2, 3]], [1, 2, 3])

assert is_equal_sets([[1, 2]], [[2, 1]])

assert not is_equal_sets(
    [make_pair(1, 2)],
    [make_pair(2, 1)]
)


# ============================================================
# 8. cartesian_product()
# ============================================================

assert cartesian_product([], [1, 2]) == []

assert cartesian_product([1, 2], []) == []

assert cartesian_product([1], [2]) == [(1, 2)]

product = cartesian_product([1, 2, 3], [1, 2, 3])

assert is_set(product)

assert set(product) == {
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
}

assert_same_set(
    cartesian_product([1, []], [1, []]),
    [
        (1, 1),
        (1, []),
        ([], 1),
        ([], [])
    ]
)


# ============================================================
# 9. union_sets()
# ============================================================

union_result = union_sets([1, 2, 3], [1, 2, 3])

assert is_set(union_result)

assert set(union_result) == set([1, 2, 3]).union(
    set([1, 2, 3])
)


union_result = union_sets([1, 2, 3], [1, 2, 3, 4])

assert is_set(union_result)

assert set(union_result) == set([1, 2, 3]).union(
    set([1, 2, 3, 4])
)


assert_same_set(
    union_sets([1, 2], [2, 3]),
    [1, 2, 3]
)

assert_same_set(
    union_sets([], [1, 2]),
    [1, 2]
)

assert_same_set(
    union_sets([1, 2], []),
    [1, 2]
)

assert_same_set(
    union_sets([1, 2], [1, 2]),
    [1, 2]
)

assert_same_set(
    union_sets([1, 2, 3], [1, 2, 3, []]),
    [1, 2, 3, []]
)

assert_same_set(
    union_sets([[1, 2]], [[2, 1], [3, 4]]),
    [[1, 2], [3, 4]]
)


# Комутативність: A ∪ B = B ∪ A

assert_same_set(
    union_sets([1, 2], [2, 3]),
    union_sets([2, 3], [1, 2])
)


# Ідемпотентність: A ∪ A = A

assert_same_set(
    union_sets([1, 2], [1, 2]),
    [1, 2]
)


# ============================================================
# 10. intersection_sets()
# ============================================================

intersection_result = intersection_sets(
    [1, 2, 3],
    [1, 2, 3, []]
)

assert is_set(intersection_result)

assert set(intersection_result) == {1, 2, 3}


assert_same_set(
    intersection_sets([], [1, 2, 3]),
    []
)

assert_same_set(
    intersection_sets([1, 2, 3], []),
    []
)

assert_same_set(
    intersection_sets([1, 2, 3], [4, 5, 6]),
    []
)

assert_same_set(
    intersection_sets([[]], [1, 2, 3, []]),
    [[]]
)

assert_same_set(
    intersection_sets([1, 2, 3], [2, 3, 4]),
    [2, 3]
)

assert_same_set(
    intersection_sets(
        [[1, 2], [3, 4]],
        [[2, 1], [5, 6]]
    ),
    [[1, 2]]
)


# Комутативність: A ∩ B = B ∩ A

assert_same_set(
    intersection_sets([1, 2, 3], [2, 3, 4]),
    intersection_sets([2, 3, 4], [1, 2, 3])
)


# Ідемпотентність: A ∩ A = A

assert_same_set(
    intersection_sets([1, 2], [1, 2]),
    [1, 2]
)


# ============================================================
# 11. diffence_sets()
# ============================================================

difference_result = difference_sets([1, 2, 3], [2, 4])

assert is_set(difference_result)

assert set(difference_result) == {1, 3}


assert_same_set(
    difference_sets([1, 2, 3], [1, 2, 3]),
    []
)

assert_same_set(
    difference_sets([1, 2, 3], []),
    [1, 2, 3]
)

assert_same_set(
    difference_sets(
        [[1, 2], [3, 4]],
        [[2, 1], [5, 6]]
    ),
    [[3, 4]]
)


# (A \ B) ∩ B = ∅

difference = difference_sets([1, 2, 3], [2, 4])

assert_same_set(
    intersection_sets(difference, [2, 4]),
    []
)


# ============================================================
# 12. complement_set()
# ============================================================

A = [1, 2, 3, []]
U = [1, 2, 3, 4, [], [[]]]

assert is_set(A)
assert is_set(U)

assert_same_set(
    complement_set(A, U),
    [4, [[]]]
)


# Доповнення порожньої множини: U \ ∅ = U

assert_same_set(
    complement_set([], [1, 2, 3]),
    [1, 2, 3]
)


# Доповнення універсальної множини: U \ U = ∅

assert_same_set(
    complement_set([1, 2, 3], [1, 2, 3]),
    []
)


# Закон подвійного доповнення:
# U \ (U \ A) = A

universal = [1, 2, 3, 4]
subset = [1, 3]

assert_same_set(
    complement_set(
        complement_set(subset, universal),
        universal
    ),
    subset
)


# Перевірка ValueError, якщо A не є підмножиною U

try:
    complement_set([4], [1, 2, 3])
except ValueError:
    pass
else:
    raise AssertionError("Expected ValueError")


# ============================================================
# 13. powerset()
# ============================================================

assert_same_set(
    powerset([]),
    [[]]
)

assert_same_set(
    powerset([1]),
    [[], [1]]
)

assert_same_set(
    powerset([1, 2]),
    [[], [1], [2], [1, 2]]
)

assert_same_set(
    powerset([1, 2, 3]),
    [
        [],
        [1],
        [2],
        [3],
        [1, 2],
        [1, 3],
        [2, 3],
        [1, 2, 3]
    ]
)

assert_same_set(
    powerset([[1, 2]]),
    [[], [[1, 2]]]
)
assert cardinality(powerset([1, 2, 3])) == 2**cardinality([1, 2, 3])