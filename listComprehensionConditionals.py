""" conditional expressions in list comprehensions
"""

"""
https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals
"""
lst = [1, 2, 3, 4, 5]
print [i for i in lst]
print ['yes' if (i == 1) else 'no' if (i == 2) else 'idle' for i in lst]
#['yes', 'no', 'idle', 'idle', 'idle']



"""
https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
"""
#You can also put the conditional expression in brackets inside the list comprehension:
l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
print [[x+5,x+1][x >= 45] for x in l]
# [false,true][condition] is the syntax


