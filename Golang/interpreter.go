package main

import (
	"fmt"
)

func interpreter(bf_code string) {
	pointer := 0
	tape := make([]int, 0)

	for i := 0; i <= 30; i++ {
		tape = append(tape, 0)
	}

	runes := []rune(bf_code)

	for i := 0; i < len(runes); i++ {
		char := string(runes[i])
		if char == "+" {
			tape[pointer] += 1
		}
		if char == "-" {
			if pointer > 0 {
				tape[pointer] -= 1
			}
		}
		if char == ">" {
			pointer += 1
		}
		if char == "<" {
			if pointer > 0 {
				pointer -= 1
			}
		}
		if char == "." {
			fmt.Printf("%v", string(rune(tape[pointer])))
		}
		// if char == "," {
		// 	var input string
		// 	fmt.Scanln(&input)

		// }
	}
}
