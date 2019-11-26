import pytest
from factorial import factorial

def testFactorial1():
    assert factorial.factorial(3628800) == 10

def testFactorial2():
    assert factorial.factorial(40320) == 8

def testFactorial3():
    assert factorial.factorial(6) == 3

def testFactorialNone():
    assert factorial.factorial(18) == "NONE"
