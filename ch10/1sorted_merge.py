def sorted_merge(a, b):
    insert_idx = len(a) - 1
    b_idx = len(b) - 1
    a_idx = len(a) - len(b) - 1

    while b_idx >= 0:
        if a_idx >= 0 and a[a_idx] > b[b_idx]:
            a[insert_idx] = a[a_idx]
            a_idx -= 1
        else:
            a[insert_idx] = b[b_idx]
            b_idx -= 1
        if insert_idx > 0:
            insert_idx -= 1
    return a

a = [9, 10, 11, 12, 13, 0, 0, 0, 0]
b = [4, 5, 6, 7]
print(sorted_merge(a,b)) #[4, 5, 6, 7, 9, 10, 11, 12, 13]
