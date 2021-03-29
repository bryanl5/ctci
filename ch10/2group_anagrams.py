#leetcode 49
from collections import defaultdict
def group(str_array):
    d = defaultdict(list)
    for word in str_array:
        d[tuple(sorted(word))].append(word)
    return d.values()

words = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]
print(group(words))