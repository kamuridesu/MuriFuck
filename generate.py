def generate(string):
	string = [ord(x) for x in string]
	increase = ""
	for x in string:
		increase += "+" * x
		increase += "\n"
		increase += ">"
	increase += "\n"
	for _ in string:
		increase += "<"
	increase += "\n"
	for _ in range(len(string)):
		increase += ". >"
	return increase


print(generate(""))