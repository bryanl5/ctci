def triple_step(steps, memo):
    if(steps < 0):
        return 0
    if(steps == 0):
        return 1
    if steps in memo:
        return memo[steps]
    memo[steps] = triple_step(steps - 1, memo) + triple_step(steps - 2, memo) + triple_step(steps - 3, memo)

    return memo[steps]

memo = {}
print(triple_step(0, memo)) #1
memo = {}
print(triple_step(1, memo)) #1
memo = {}
print(triple_step(-1, memo)) #0
memo = {}
print(triple_step(3, memo)) #4