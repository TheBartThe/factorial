import pytest
from factorial import factorial

def testFactorial1():
    assert factorial.fact(3628800) == 10

def testFactorial2():
    assert factorial.fact(40320) == 8

def testFactorial3():
    assert factorial.fact(6) == 3

def testFactorial4():
    assert factorial.fact(24) == 4

def testFactorialNone():
    assert factorial.fact(18) == "NONE"

def testFactorialLarge():
    assert factorial.fact(479001600) == 12

def testFactorial5():
    assert factorial.fact(720) == 6
