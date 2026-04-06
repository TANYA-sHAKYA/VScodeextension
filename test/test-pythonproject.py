# This file intentionally contains multiple issues for linting

import os, sys   # multiple imports in one line (bad practice)

x = 10
y = "Hello"

def add(a, b):
    return a + b

def unused_function():
    temp = 5   # unused variable
    return temp

def type_issue(a: int, b: int) -> int:
    return a + "string"   # type error

def bad_naming():
    BADvariableName = 5   # bad naming convention
    return BADvariableName

def indentation_issue():
  print("Wrong indentation")   # indentation issue

def unreachable_code():
    return True
    print("This will never execute")  # unreachable code

z = add(x, y)   # type mismatch

print("Done")