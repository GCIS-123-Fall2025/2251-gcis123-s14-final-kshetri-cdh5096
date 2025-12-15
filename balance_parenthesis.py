
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
# from node_stack import Stack

from node_stack import *

def balance_parenthesis(a_string):
    # stack = Stack()
    a = Stack()
    balance = 0
    for character in a_string:
        if character == "(" or character == ")":
            a.push(character)
    for i in range(len(a)):
        character = a.pop()
        if character == "(":
            balance += 1
            if balance > 0:
                return i
        elif character == ")":
            balance -= 1
    if balance < 0:
        return -1
    if balance == 0:
        return 0


def main():     
    print(balance_parenthesis("--(---(------)--")) # 2
    print(balance_parenthesis("()----)")) # -1
    print(balance_parenthesis("-----()--(())")) # 0

if __name__ == "__main__":    main()