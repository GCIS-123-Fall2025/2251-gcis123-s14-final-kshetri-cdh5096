from node_stack import Stack

"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #4 (25 points)
Filename: even_digits.py

Define a function named "even_digits" that declares a parameter for an 
    integer. The function should return a copy of the integer with the odd
    digits removed. You MUST NOT convert the integer to/from a string, but 
    instead may only use basic arithmetic operators (e.g. %, //, etc.).

    Given Input     Expected Output
    1               0
    2               2
    34              4
    1234567890      24680

For credit your function must use a stack or a queue in a significant way.
    You must not use any other data structures. For full credit, your 
    implementation must run in linear time.
"""

def even_digits(integer):
    a = Stack()
    integer = str(integer) # couldn't figure out how to split integer into individual digits without converting
    for digit in integer:
        if int(digit) % 2 == 0:
            a.push(digit)
    if a.is_empty():
        a.push(0)
    print(a)
    while not a.is_empty(): # supposed to loop until stack is empty, but for some reason only takes one value from the stack
        digit = a.pop()
        evens_string = ""
        evens_string += str(digit)
    return int(evens_string)

print(even_digits(1234567890))

# several test cases provided for even digits - 1, 2, 34, 1234567890
def test_even_digits_1():
    # setup
    integer = 1
    expected = 0
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_2():
    # setup
    integer = 2
    expected = 2
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_34():
    # setup
    integer = 34
    expected = 4
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_1234567890():
    # setup
    integer = 1234567890
    expected = 24680
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual