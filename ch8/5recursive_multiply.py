def product(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b

    return rec_product(smaller, bigger)

def rec_product(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    
    s = smaller >> 1 
    half = rec_product(s, bigger)
    if smaller % 2 == 0:
        return half + half
    else:
        return half + half + bigger

print(product( 25, 13)) #325
print(product( 13, 25)) #325
print(product(0, 134)) #0
print(product(0, 0)) #0

#15 min thinking
#10 min coding