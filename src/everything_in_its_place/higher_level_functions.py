from everything_in_its_place.base_functions import add

def add_loop(a, b, n):
    result = 0
    for idx in range(n):
        result = add(result, add(a[idx], b[idx]))
    return result