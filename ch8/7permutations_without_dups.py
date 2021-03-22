def get_perms(string):
    permutations = []
    if len(string) == 0:
        permutations.append(" ")
        return permutations
    
    first_char = string[0]
    rest = string[1:]
    ealier_perms = get_perms(rest)
    for perm in ealier_perms:
        for i in range(len(perm)):
            before = perm[:i]
            after = perm[i:]
            permutations.append(before + first_char + after)
    return permutations

print(get_perms("abc")) #['abc ', 'bac ', 'bca ', 'acb ', 'cab ', 'cba ']
print(get_perms("")) #[" "]
