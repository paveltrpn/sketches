package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"unicode"
)

type stringBuf_s struct {
	pos int
	str string
}

func buildStringBuf(str string) stringBuf_s {
	return stringBuf_s{0, str}
}

func (sb *stringBuf_s) getNextChar() (int, int) {
	if sb.pos+1 > len([]rune(sb.str)) {
		return -1, int(' ')
	}

	rt := sb.str[sb.pos]
	sb.pos = sb.pos + 1
	return sb.pos, int(rt)
}

func (sb *stringBuf_s) loadNewString(new string) {
	sb.str = new
	sb.pos = 0
}

var (
	lookahead int
	stringBuf stringBuf_s
)

func expr() {
	term()
	for true {
		if lookahead == '+' {
			match('+')
			term()
			fmt.Print("+")
		} else if lookahead == '-' {
			match('-')
			term()
			fmt.Print("-")
		} else {
			return
		}
	}
}

func term() {
	if unicode.IsNumber(rune(lookahead)) {
		t := lookahead
		match(lookahead)
		fmt.Print(string(t))
	} else {
		fmt.Printf("syntax error in term()! %v - is not number!\n", string(lookahead))
		os.Exit(1)
	}
}

func match(t int) {
	if lookahead == t {
		_, lookahead = stringBuf.getNextChar()
	} else {
		fmt.Println("syntax error in match()!")
		os.Exit(1)
	}
}

func readOneRune(rd io.Reader) rune {
	in := bufio.NewReader(rd)
	foo, _, _ := in.ReadRune()

	return foo
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("read: ")
	text, _ := reader.ReadString('\n')

	if len([]rune(text)) > 1 {
		stringBuf = buildStringBuf(text)
	} else {
		// Use default string
		stringBuf = buildStringBuf("8-5+3+1-5")
	}

	_, lookahead = stringBuf.getNextChar()

	expr()
	fmt.Println()
}
