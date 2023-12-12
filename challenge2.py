def exactly_two_positive(a, b, c):
    positive_count = (a > 0) + (b > 0) + (c > 0)
    return positive_count == 2
