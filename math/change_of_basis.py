def sum_of_vectors(v, w):
    result = []
    i = 0
    while i < len(v):
        result.append(v[i]+w[i])
        i = i + 1
    return result

def is_equal_lists(l1, l2, tolerance = 1e-9):
    if len(l1) != len(l2):
        raise ValueError("Lists must have same length")
    i = 0
    while i < len(l1):
        if isinstance(l1[i], float) or isinstance(l2[i], float):
            if abs(l1[i]) < tolerance or abs(l2[i]) < tolerance:
                if abs(l1[i]-l2[i]) > tolerance:
                    return False
            else:
                if abs((l1[i]-l2[i])/l1[i]) > tolerance:
                    return False
        else:
            if l1[i] != l2[i]:
                return False
        i = i + 1
    return True

def combine(a, b, b1, b2):
    a_transf = [a*x for x in b1]
    b_transf = [b*x for x in b2]
    return sum_of_vectors(a_transf, b_transf)

def coords(v, b1, b2):
    x = v[0]
    y = v[1]
    p = b1[0]
    q = b1[1]
    r = b2[0]
    s = b2[1]
    det = s*p - q*r

    if abs(det) < 1e-9:
        raise ValueError("Determinant == 0")
    a_new = (r*y - s*x) / (q*r - s*p)
    b_new = (p*y - q*x) / (det)

    assert is_equal_lists(combine(a_new, b_new, b1, b2), list(v))
    return [a_new, b_new]

assert is_equal_lists(coords([7, 4], [0, 1], [1, 0]), [4, 7])
assert is_equal_lists(coords([7, 4], [1, 2], [0, 1]), [7, -10])
assert is_equal_lists(coords([3, 5], [0, 1], [1, 1]), [2, 3])
assert is_equal_lists(coords([3, 1], [1, 1], [1, -1]), [2, 1])
assert is_equal_lists([1e-17, 5.0], [0, 5])
assert is_equal_lists([5.55e-17, 5.0], [0, 5])

try:
    coords([3, 6], [1, 2], [2, 4])
    raised = False
except ValueError:
    raised = True
assert raised

try:
    coords([3, 6], [1, 1], [0.1 + 0.2, 0.3])
    raised = False
except ValueError:
    raised = True
assert raised