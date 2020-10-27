#_____________________________________________________________________________________ 00
"""
FILTER BY CONDITION
"""

import statistics

lengthMap = map(lambda v: v.GetLength(),crvsRC)
print "averageLength = " + str(statistics.mean(lengthMap))
averageLen = statistics.mean(lengthMap)
longerLengths = filter((lambda v: True if (v > averageLen) else False),lengthMap)


#_____________________________________________________________________________________ 01
"""
FILTER LIST BY BOOELAN LIST

https://www.geeksforgeeks.org/python-filter-list-by-boolean-list/
https://stackoverflow.com/questions/18665873/filtering-a-list-based-on-a-list-of-booleans
15:02 27.10.2020
"""

import itertools
from itertools import compress

list_a = [1, 2, 4, 6]
fil = [True, False, True, False]
list(compress(list_a, fil))


#_____________________________________________________________________________________ 02
"""
ASSOCIATIVE SORT

https://stackoverflow.com/questions/54651371/sorting-2-lists-that-are-related-using-zip-function-in-python-how-to-sort-in-de/54651441
"""

numLst_sorted, stuffLst_sorted = zip(*sorted(zip(numLst,stuffLst)))

candidates = ['Donald', 'Barack', 'Hillary', 'Mitt']
votes = [9, 7, 1, 3]
print(sorted(zip(candidates, votes), reverse=True))
# [('Mitt', 3), ('Hillary', 1), ('Donald', 9), ('Barack', 7)]

print zip(*sorted(zip(candidates, votes), reverse=True))
# [('Mitt', 'Hillary', 'Donald', 'Barack'), (3, 1, 9, 7)]

#_____________________________________________________________________________________ 03
"""

"""

