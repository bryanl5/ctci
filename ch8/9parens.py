#leetcode https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
def parens(n):
    results = []
    left, right  = n, n
    parens_helper(left, right, results, "")
    return results

def parens_helper(left, right, result, string):
    if right < left:
        return
    if right == 0 and left == 0:
        result.append(string)
    if right > 0:
        parens_helper(left, right - 1, result, string + ")")
    if left > 0:
        parens_helper(left - 1, right, result, string + "(")

print(parens(3))
