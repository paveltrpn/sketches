package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"unicode"
)

var lookahead rune

func expr() {
	term()
	for true {
		if lookahead == '+' {
			match('+')
			term()
			fmt.Println("+")
		} else if lookahead == '-' {
			match('-')
			term()
			fmt.Println("-")
		} else {
			return
		}
	}
}

func term() {
	if unicode.IsNumber(lookahead) {
		t := lookahead
		match(lookahead)
		fmt.Println(string(t))
	} else {
		fmt.Printf("syntax error in term()! %v - is not number!\n", string(lookahead))
		os.Exit(1)
	}
}

func match(t rune) {
	if lookahead == t {
		fmt.Print("read:")
		lookahead = readOneRune(os.Stdin)
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
	fmt.Print("read:")
	lookahead = readOneRune(os.Stdin)

	expr()
	fmt.Println()
}
