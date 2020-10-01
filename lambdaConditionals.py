"""
https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/
"""

# 01 | Using if else in Lambda function

# Lambda function to check if a given vaue is from 10 to 20.
test = lambda x : True if (x > 10 and x < 20) else False

# 02 | Creating conditional lambda function without if else

# Lambda function to check if a given vaue is from 10 to 20.
check = lambda x : x > 10 and x < 20
