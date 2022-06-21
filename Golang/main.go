package main

func main() {
	arguments := getCliArgs()
	interpreter(generateBFCode(arguments))
}
