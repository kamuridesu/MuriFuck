package main

func generateBFCode(text string) string {
	runes := []rune(text)
	bf_code := ""
	for i := 0; i < len(runes); i++ {
		char := runes[i]
		for i := 0; i < int(char); i++ {
			bf_code = bf_code + "+"
		}
		bf_code = bf_code + "\n>"
	}
	bf_code = bf_code + "\n"
	for i := 0; i < len(runes); i++ {
		bf_code = bf_code + "<"
	}
	for i := 0; i < len(runes); i++ {
		bf_code = bf_code + ". >"
	}
	return bf_code
}
