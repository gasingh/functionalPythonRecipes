"""
https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/
"""

# ------------------------------------------------------------------------------
# 01 | Using if else in Lambda function

# Lambda function to check if a given vaue is from 10 to 20.
test = lambda x : True if (x > 10 and x < 20) else False

# ------------------------------------------------------------------------------
# 02 | Creating conditional lambda function without if else

# Lambda function to check if a given vaue is from 10 to 20.
check = lambda x : x > 10 and x < 20

# ------------------------------------------------------------------------------
# 03 | Using if, elif & else in a lambda function

# Lambda function with if, elif & else i.e.
# If the given value is less than 10 then Multiplies it by 2
# else if it's between 10 to 20 the multiplies it by 3
# else returns the unmodified same value
converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)

def converter(x):
  if x<10:
    # CONDITION 1
    return x*2
  elif x<20:
    # CONDITION 2
    return x*3
  else:
    # CONDITION 3
    return x

# converter = lambda v : OUT1 if (CONDITION 1) else(OUT2 if (CONDITION 2) else OUT3)
# ------------------------------------------------------------------------------



