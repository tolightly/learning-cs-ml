def myset(lst: list) -> list:
    count = 0
    length = cardinality(lst)
    result = []
    while count < length:
        if not is_member(lst[count], result):
            result.append(lst[count])
        count = count + 1
    return result

def cardinality(set: list) -> int:
    return len(set)

def no_dubs(set: list) -> bool:
    i = 0
    i_max = cardinality(set)
    while i < i_max:
        j = i + 1
        while j < i_max:
            if set[i] == set[j]:
                return False
            j = j + 1
        i = i + 1
    return True

def is_member(element, set: list) -> bool:
    i = 0
    i_max = cardinality(set)
    while i < i_max:
        if element == set[i]:
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
    if cardinality(set1) != cardinality(set2):
        return False
    i = 0
    i_max = cardinality(set1)
    j = 0
    j_max = cardinality(set2)
    while i < i_max:
        if not is_member(set1[i], set2):
            return False
        i = i + 1
    return True

def cartesian_product(set1: list, set2: list) -> list:
    i = 0
    i_max = cardinality(set1)
    j_max = cardinality(set2)
    result = []
    while i < i_max:
        j = 0
        while j < j_max:
            result.append([set1[i], set2[j]])
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
    return result

def complement_set(set: list, universal: list) -> list:
    i = 0
    i_max = cardinality(universal)
    result = []
    while i < i_max:
        if not is_member(universal[i], set):
            result.append(universal[i])
        i = i + 1
    return result

#def powerset(set: list) -> list:


l_1 = [1, 2, [2, 3], 3, [4, 4], [3, 2], 5, [2, [2, 3]], [2, 3]]
l_2 = [[4, 4], 5, 6, 7, 8, 9]
eq_1 = [1, 2, [2, 3], 3, [4, 4], 5]
eq_2 = [[4, 4], 3, 1, 5, 2, [2, 3]]
subs_1 = [1, 2, 3]
subs_2 = [1, 3, 7, 2, 4, 5, 6]
subs_3 = [1, [3, 2]]
s_1 = myset(l_1)
s_2 = myset(l_2)
print("list is: ", l_1)
print("myset is: ", s_1)
print("cardinality is: ", cardinality(s_1))
print("is 4 in set?", is_member(4, s_1))
print("is [4, 4] in set?", is_member([4, 4], s_1))
print("is [3, 4] in set?", is_member([3, 4], s_1))
print("is 6 in set?", is_member(6, s_1))
print("is None in set?", is_member(None, s_1))
print("Cartesian product: ", cartesian_product(s_1, s_2))
print("Union sets: ", union_sets(s_1, s_2))
print("Intersection sets: ", intersection_sets(s_1, s_2))
print("Is equal? ", is_equal_sets(eq_1, eq_2))
print("Is subset? ", is_subset(subs_3, s_1))
print("Difference of sets: ", diffence_sets(s_1, s_2))
print("Complement: ", complement_set(s_1, s_2))
#rint("No dubs: ", no_dubs(l_1))
