
import numbers
from pickle import TRUE

lookahead: str = ""

def expr() -> None:
    term()
    while TRUE:
        if lookahead == "+":
            match("+")
            term()
            print("+")
        elif lookahead == "-":
            match("-")
            term()
            print("-")
        else:
            return

def term() -> None:
    if lookahead.isnumeric():
        t = lookahead
        match(lookahead)
        print(t)
    else:
        print("syntax error in term()! {} - is not number!".format(lookahead))
        exit()

def match(t: str) -> None:
    global lookahead
    if lookahead == t:
        print("read:", end="")
        lookahead = input()
    else:
        print("syntax error in match!")
        exit(0)


def main() -> None:
    global lookahead
    print("read:", end="")
    lookahead = input()

    expr()
    print()

if __name__ == "__main__":
    main()