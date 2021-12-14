package main

import (
	"file_io/internal/read"
	"fmt"
)

func main() {
	println("Golang file IO test")
	foo := read.TextRead("../assets/raven.txt")

	println(foo[:100])

	bar := read.TextReadLines("../assets/raven.txt")
	for i := range bar {
		fmt.Printf("%v: %v\n", i, bar[i])

		if i >= 1 {
			break
		}
	}
}
