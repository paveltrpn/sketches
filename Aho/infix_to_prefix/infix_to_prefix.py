
from expression_string import *


foo: expressionString_c = expressionString_c("9-5+2-1+7")
lookahead: str = ""
stash: str = ""

def expr() -> None:
    global lookahead
    global stash
    term()
    while True:
        if lookahead == "+":
            print("+", end="")
            lookahead = foo.getNextChar()[1]
            term()
            stash = ""
        elif lookahead == "-":
            print("-", end="")
            lookahead = foo.getNextChar()[1]
            term()
            stash = ""
        else:
            return

def term() -> None:
    global lookahead
    global stash

    print(stash, end="")
    if lookahead.isnumeric():
        stash = lookahead
        print(lookahead, end="")
        lookahead = foo.getNextChar()[1]
    else:
        print("syntax error in term()! {} - is not number!".format(lookahead))
        exit()

def main() -> None:
    print("read: ", end="")
    inputStr = input()

    if len(inputStr) > 0:
        foo.loadNewString(inputStr)

    global lookahead
    global stash
    lookahead = foo.getNextChar()[1]
    stash = ""

    expr()
    print()

if __name__ == "__main__":
    main()