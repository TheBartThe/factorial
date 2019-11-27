import pytest
from factorial import factorial as fact

def testFactorial1():
    assert fact.factorial(3628800) == 10

def testFactorial2():
    assert fact.factorial(40320) == 8

def testFactorial3():
    assert fact.factorial(6) == 3

def testFactorial4():
    assert fact.factorial(24) == 4

def testFactorialNone():
    assert fact.factorial(18) == "NONE"

def testFactorialLarge():
    assert fact.factorial(479001600) == 12

def testFactorial5():
    assert fact.factorial(720) == 6
