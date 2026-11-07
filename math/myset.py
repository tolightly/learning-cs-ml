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
    return myset(result)

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
    return myset(result)

def diffence_sets(set1: list, set2: list) -> list:
    i = 0
    i_max = cardinality(set1)
    result = []
    while i < i_max:
        if not is_member(set1[i], set2):
            result.append(set1[i])
        i = i + 1
    return myset(result)

def complement_set(set: list, universal: list) -> list:
    if not is_subset(set, universal):
            raise ValueError("Set must be a subset of universal")
    return diffence_sets(universal, set)

# def powerset(set: list) -> list:

# Asserts
assert(no_dubs([[], []])) == False
assert(no_dubs([[2, 3], [3, 2]])) == False
assert(no_dubs([[2, 3], [2, [2, 3]]])) == True
assert(no_dubs([make_pair(1, 2), make_pair(2, 1)])) == True
assert(is_member([], [1, 2, 3])) == False
assert(is_member([], [[], 1, 2, 3])) == True
assert(is_member([2, 3], [[3, 1], [1, [2, 3]]])) == False
assert(is_member([2, 3], [[3, 2], [1, [2, 1]]])) == True
assert(is_member(make_pair(2, 3), [make_pair(3, 2)])) == False
assert(is_member(make_pair(2, 3), [make_pair(2, 3)])) == True
assert(is_subset([], [1, 2])) == True
assert(is_subset([[3, 4]], [2, 3, 4])) == False
assert(is_subset([[3, 4]], [2, [3, 4]])) == True
assert(is_subset([make_pair(1, 2)], [make_pair(2, 1), make_pair(1, 1)])) == False
assert(is_subset([make_pair(1, 2)], [make_pair(1, 2), make_pair(1, 1)])) == True
assert(is_equal_sets([], [[]])) == False
assert(is_equal_sets([1, 1, 2], [1, 2])) == True
assert(is_equal_sets([1, [2, 3]], [1, 2, 3])) == False
assert(is_equal_sets([make_pair(1, 2)], [make_pair(2, 1)])) == False
assert(cardinality(cartesian_product([1, 2, 2, 3], [1, 2, 1, 3]))) == 9
assert(cardinality(cartesian_product([1, []], [1, []]))) == 4
assert(cardinality(union_sets([1, 2, 3], [1, 2, 3]))) == 3
assert(cardinality(union_sets([1, 2, 3], [1, 2, 3, []]))) == 4
assert(cardinality(intersection_sets([1, 2, 2, 3], [1, 2, 3, 3, []]))) == 3
assert(cardinality(intersection_sets([], [1, 2, 3, []]))) == 0
assert(cardinality(intersection_sets([[]], [1, 2, 3, []]))) == 1
assert(cardinality(diffence_sets([1, 2, 3, 2], [1, 2, 3, []]))) == 0
assert(cardinality(diffence_sets([1, 2, 3, 3, []], [1, 2, 3]))) == 1
assert(cardinality(diffence_sets([1, 2, 3, 3, []], [1, 2, 3, 4, 4, 1, 2, [], [[]]]))) == 2
