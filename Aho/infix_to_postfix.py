
class stringBuf_c:
    def __init__(self, line: str) -> None:
        self.pos: int = 0
        self.string: str = line

    def getNextChar(self) -> tuple[int, str]:
        if self.pos+1 > len(self.string):
            return -1, ""

        rt = self.string[self.pos]
        self.pos = self.pos + 1
        return self.pos, rt

    def setPos(self, pos: int) -> int:
        if pos > len(self.string) or pos < 0:
            return -1
        self.pos = pos
        return 0

    def loadNewString(self, new: str) -> None:
        self.string = new
        self.pos = 0

foo: stringBuf_c = stringBuf_c("3+8+2-4+9-1")
lookahead: str = ""

def expr() -> None:
    term()
    while True:
        if lookahead == "+":
            match("+")
            term()
            print("+", end="")
        elif lookahead == "-":
            match("-")
            term()
            print("-", end="")
        else:
            return

def term() -> None:
    if lookahead.isnumeric():
        t = lookahead
        match(lookahead)
        print(t, end="")
    else:
        print("syntax error in term()! {} - is not number!".format(lookahead))
        exit()

def match(t: str) -> None:
    global lookahead
    if lookahead == t:
        lookahead = foo.getNextChar()[1]
    else:
        print("syntax error in match!")
        exit(0)


def main() -> None:
    print("read: ", end="")
    inputStr = input()

    if len(inputStr) > 0:
        foo.loadNewString(inputStr)

    global lookahead
    lookahead = foo.getNextChar()[1]

    expr()
    print()

if __name__ == "__main__":
    main()