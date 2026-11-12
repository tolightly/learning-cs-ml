def sum_of_vectors(v, w):
    result = []
    i = 0
    while i < len(v):
        result.append(v[i]+w[i])
        i = i + 1
    return result
def is_equal_lists(l1, l2, tolerance = 1e-6):
    if len(l1) != len(l2):
        raise ValueError("Lists must have same length")
    i = 0
    while i < len(l1):
        if isinstance(l1[i], float) or isinstance(l2[i], float):
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

    if p == 0:
        raise ValueError("p == 0 leads to ZeroDivisionError")
    
    if q/p == s/r:
        raise ValueError("Colinear vectors")

    b_new = (p*y - q*x) / (s*p - q*r)
    a_new = (x - b_new*r) / p
    assert is_equal_lists(combine(a_new, b_new, b1, b2), list(v))
    return [a_new, b_new]

print(combine(7, 4, [1, 2], [3, 1]))
print(coords([7, 4], [1, 2], [3, 1]))
coords([7, 4], [1, 2], [2, 4])