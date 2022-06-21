package main

import (
	"os"
	"strings"
)

func getCliArgs() string {
	if len(os.Args) >= 2 {
		return strings.Join(os.Args[1:], " ")
	}
	panic("Error! No arguments provided")
}
