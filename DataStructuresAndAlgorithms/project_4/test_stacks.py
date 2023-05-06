import pytest
from stack import Stack
from main import eval_postfix as epf
from main import in2post as i2p
import io
import sys

def test_stack_creation():
    stk = Stack()
    assert stk.size() == 0
    with pytest.raises(IndexError):
        stk.pop()

def test_stack_push_pop():
    stk = Stack()
    stk.push(1)
    stk.push(3.14)
    stk.push("cat")
    assert stk.size() == 3
    stk.top() == "cat"
    stk.size() == 3
    stk.pop() == "cat"
    assert stk.size() == 2
    assert stk.pop() == 3.14
    assert stk.pop() == 1
    assert stk.size() == 0
    with pytest.raises(IndexError):
        stk.top()
    with pytest.raises(IndexError):
        stk.pop()

    for i in range(100):
        stk.push(i)
    assert stk.size() == 100
    stk.clear()
    stk.size() == 0

def test_equation_1():
    assert epf("4") == 4.0

def test_equation_2():
    assert epf("5 7 +") == 12.0

def test_equation_3():
    assert epf("5 7 *") == 35.0

def test_equation_4():
    assert epf("5 3 -") == 2.0

def test_equation_5():
    assert epf("5 5 /") == 1.0

def test_equation_6():
    assert epf("8 5 * 3 +") == 43.0

def test_equation_7():
    assert epf("8 5 3 + *") == 64.0

def test_equation_8():
    assert epf("8 3 5 * + 7 -") == 16.0

def test_equation_9():
    assert epf("8 3 + 5 6 - *") == -11.0

def test_equation_10():
    assert epf("8 3 + 2 7 - *") == -55.0

def test_equation_11():
    assert epf("8 3 + 2 * 7 -") == 15.0

def test_equation_12():
    assert epf("8 5 * 3 2 - 7 3 * - +") == 20.0

def test_equation_13():
    assert epf("8 5 * 3 + 7 - 5 3 * -") == 21.0

def test_equation_14():
    assert epf(" 7 9 * 7 + 5 6 * - 3 + 4 -") == 39.0

def test_bad_postfix():
    with pytest.raises(SyntaxError):
        epf(" 7 9 * 7 + 5 6 * - 3 + 4 -+")
    with pytest.raises(ValueError):
        epf(None)


def test_infix_1():
    postfix = i2p("4")
    assert postfix.replace(" ", "") == "4"

def test_infix_2():
    postfix = i2p("5  +7")
    assert postfix.replace(" ", "") == "5 7 +".replace(" ", "")

def test_infix_3():
    postfix = i2p("7*5")
    assert postfix.replace(" ", "") == "7 5 *".replace(" ", "")

def test_infix_4():
    postfix = i2p("(5-3)")
    assert postfix.replace(" ", "") == "5 3 -".replace(" ", "")

def test_infix_5():
    postfix = i2p("5/5")
    assert postfix.replace(" ", "") == "5 5 /".replace(" ", "")

def test_infix_6():
    postfix = i2p("8*5+3")
    assert postfix.replace(" ", "") == "8 5 * 3 +".replace(" ", "")

def test_infix_7():
    postfix = i2p("8*(5+3)")
    assert postfix.replace(" ", "") == "8 5 3 + *".replace(" ", "")

def test_infix_8():
    postfix = i2p("8+3*5-7")
    assert postfix.replace(" ", "") == "8 3 5 * + 7 -".replace(" ", "")

def test_infix_9():
    postfix = i2p("(8+3)*(5-6)")
    assert postfix.replace(" ", "") == "8 3 + 5 6 - *".replace(" ", "")

def test_infix_10():
    postfix = i2p("((8+3)*(2-7))")
    assert postfix.replace(" ", "") == "8 3 + 2 7 - *".replace(" ", "")

def test_infix_11():
    postfix = i2p("((8+3)*2)-7")
    assert postfix.replace(" ", "") == "8 3 + 2 * 7 -".replace(" ", "")

def test_infix_12():
    postfix = i2p("(8*5)+((3-2)-7*3)")
    assert postfix.replace(" ", "") == "8 5 * 3 2 - 7 3 * - +".replace(" ", "")

def test_infix_13():
    postfix = i2p("((8*5+3)-7)-(5*3)")
    assert postfix.replace(" ", "") == "8 5 * 3 + 7 - 5 3 * -".replace(" ", "")

def test_infix_14():
    postfix = i2p("7*9+7-5*6+3-4")
    assert postfix.replace(" ", "") == "7 9 * 7 + 5 6 * - 3 + 4 -".replace(" ", "")

def test_infix_bad_expression():
    with pytest.raises(SyntaxError):
        i2p("(8+3)*(5-6))")

def test_infix_bad_param():
    with pytest.raises(ValueError):
        i2p(None)

def test_code_quality():
    from pylint.lint import Run
    
    results = Run(['stack.py'], exit=False)
    expected = 8.5
    actual = results.linter.stats.global_note
    assert actual >= expected
