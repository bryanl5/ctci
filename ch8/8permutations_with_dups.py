def get_perms(string):
    toRtn = []
    freq_table = count_letters(string)
    get_perms_helper(freq_table, "", len(string), toRtn)
    return toRtn

def count_letters(string):
    freq = {}
    for letter in string:
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1
    return freq

def get_perms_helper(freq_table, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return
    
    for letter in freq_table:
        count = freq_table[letter]
        if count > 0:
            freq_table[letter] -= 1
            get_perms_helper(freq_table, prefix + letter, remaining - 1, result)
            freq_table[letter] = count

print get_perms("aaab")