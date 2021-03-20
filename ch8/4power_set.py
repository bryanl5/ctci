#stuck on implementation
import copy
def power_set(set, index):
    allsubsets = []
    if len(set) == index:
        allsubsets.append([])
    else:
        allsubsets = power_set(set, index + 1)
        item = set[index]
        moresubsets = []
        for i in allsubsets:
            newsubset = []
            newsubset.append(i)

            
    