# SYMBOLS
# + - < > [ ] . ,

class Brainfuck:
	def __init__(self):
		self.tape = [0 for _ in range(30)]
		self.current_location = 0

	def changeTape(self, x):
		if x == "+":
			self.tape[self.current_location] += 1
		if x == "-":
			self.tape[self.current_location] -= 1
		if x == ">":
			self.current_location += 1
		if x == "<":
			self.current_location -= 1
		if x == ".":
			print(chr(self.tape[self.current_location]), end="")
		# print(self.tape)

	def parser(self, code):
		code += " "
		skip = False
		count_len_loop = 0
		for i in range(len(code)):
			loop_code = ""
			# print(self.tape)
			x = code[i]
			if x == "[":
				loop_code = code[i + 1: code.index("]", i)]
				running = True
				while running:
					for y in loop_code:
						if self.tape[self.current_location] == 0:
							running = False
							skip = True
							break
						else:
							self.changeTape(y)
			if skip:
				if i == code.index("]", i):
					skip = False
			if skip is False:
				self.changeTape(x)
		print("\n")
			


Brainfuck().parser("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>
<<<<<<
. >. >. >. >. >. >""")

