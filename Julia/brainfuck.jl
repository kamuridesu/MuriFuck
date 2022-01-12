function Brainfuck(data)
    tape = []
    for i in 1:30
        push!(tape, 0)
    end
    pointer = 1

    function change_tape(char)
        if char == '+'
            if tape[pointer] > 255
                tape[pointer] = 1
            else
                tape[pointer] = tape[pointer] + 1
            end
        end
        if char == '-'
            if tape[pointer] < 1
                tape[pointer] = 255
            else
                tape[pointer] = tape[pointer] - 1
            end
        end
        if char == '>'
            if pointer <= size(tape, 1)
                pointer = pointer + 1
            else
                println("Error: Pointer out of bounds")
            end
        end
        if char == '<'
            if pointer - 1 >= 1
                pointer = pointer - 1
            else
                println("Error: Pointer out of bounds")
            end
        end
        if char == '.'
            print(Char(tape[pointer]))
        end
        if char == ','
            tape[pointer] = read()
        end
    end

    function parse()
        for i in 1:length(data)
            char = data[i]
            change_tape(char)

        end
    end

    parse()
end



function generateBfCode(string);
    ascii_codes = []
    code = ""
    for char in string
        push!(ascii_codes, Int(char))
    end
    for ascii_code in ascii_codes
        for i in 1:ascii_code
            code = code * "+"
        end
        code = code * "\n"
        code = code * ">"
    end
    code = code * "\n"
    for _ in ascii_codes
        code = code * "<"
    end
    code = code * "\n"
    for _ in ascii_codes
        code = code * ". >"
    end
    println(code)
    return code
end

Brainfuck(generateBfCode("Hello World!"))
