# SYMBOLS
# + - < > [ ] . ,
# > increment the data pointer (to point to the next cell to the right).
# < decrement the data pointer (to point to the next cell to the left).
# + increment (increase by one) the byte at the data pointer.
# - decrement (decrease by one) the byte at the data pointer.
# . output the byte at the data pointer.
# , accept one byte of input, storing its value in the byte at the data pointer.
# [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
# ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.

class Brainfuck:
    def __init__(self):
        # initializes our tape with 30 cells
        self.tape = [0 for _ in range(30)]
        # set the current data pointer position to 0
        self.current_location = 0

    def changeTape(self, x):
        if x == "+":
            if self.tape[self.current_location] > 255:
                self.tape[self.current_location] = 0
            else:
                self.tape[self.current_location] += 1
        if x == "-":
            if self.tape[self.current_location] <= 0:
                self.tape[self.current_location] = 255
            else:
                self.tape[self.current_location] -= 1
        if x == ">":
            if self.current_location + 1 <= len(self.tape):
                self.current_location += 1
            else:
                print("memory error: -1")
        if x == "<":
            if self.current_location - 1 >= 0:
                self.current_location -= 1
            else:
                print("memory error: -1")
        if x == ".":
            print(chr(self.tape[self.current_location]), end="")
        if x == ",":
            char = input()
            if len(char) > 0:
                char = char[0]
            self.tape[self.current_location] = ord(char)

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


if __name__ == '__main__':
    Brainfuck().parser("""+++++>+++++[<+>-].<.""")

