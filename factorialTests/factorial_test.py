import pytest
from factorial import factorial

def testFactorial1():
    assert factorial.factorial(3628800) == 10

def testFactorial2():
    assert factorial.factorial(40320) == 8

def testFactorial3():
    assert factorial.factorial(6) == 3

def testFactorial4():
    assert factorial.factorial(24) == 4

def testFactorialNone():
    assert factorial.factorial(18) == "NONE"

def testFactorialLarge():
    assert factorial.factorial(479001600) == 12

def testFactorial5():
    assert factorial.factorial(720) == 6
