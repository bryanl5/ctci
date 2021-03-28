"""
Given a number in string format, return it in number format

>>> print(stringToInt("123"))
123
>>> print(stringToInt("+123"))
123
>>> print(stringToInt("-1"))
-1

"""

def stringToInt(numStr):
    if not numStr or type(numStr) is not str or len(numStr) < 1:
        return None
    digits = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    paritySymbol = {
        "-":-1,
        "+":1
    }
    parity = 1
    startIndex = 0
    if numStr[0] in paritySymbol:
        if numStr[0] == "-":
            parity = paritySymbol[numStr[0]]
        startIndex = 1
    lenOfNum = len(numStr) - startIndex # accomodate parity
    power = lenOfNum - 1
    toRtn = 0
    for i in range(startIndex, len(numStr)): # iterating from left to right of input
        digitStr = numStr[i]
        digit = digits[digitStr]
        toRtn += digit * pow(10, power) # accomodate the fact that power(10, 0) is 1
        power -= 1
    return toRtn * parity

print(stringToInt("123"))

print(stringToInt("+123"))

print(stringToInt("-1"))