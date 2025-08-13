belt = [0]
pointer = 0
input_pointer = 0
cell_max = 300


def lexer(string, depth):
    cur_tokens = []
    while len(string) > 0:
        char = string.pop(0)
        if char in "+-,.<>@":
            cur_tokens.append(char)
        elif char == "[":
            new_tokens, new_string = lexer(string, depth + 1)
            cur_tokens.append(new_tokens)
            string = new_string
        elif char == "]":
            return cur_tokens, string
        elif char == "/":
            if string[0] == "*":
                string.pop(0); string.pop(0)
                while True:
                    if string[0] == "*":
                        if string[1] == "/":
                            string.pop(0); string.pop(0)
                            break
                    string.pop(0)

    return cur_tokens


def debug_print():
    global belt
    global pointer

    cur_belt = belt[:]
    cur_belt[pointer] = f"\033[0;32m{cur_belt[pointer]}\033[0m"

    print_string = "\n["
    for i in cur_belt[:-1]:
        print_string += f"{i}, "
    print_string += f"{cur_belt[-1]}]\n"

    print(print_string)


def parse(cur_tokens):
    global belt
    global pointer
    global input_pointer
    global cell_max
    global input_text

    count = 0
    for t in cur_tokens:
        if t == "+":
            belt[pointer] += 1
            if belt[pointer] > cell_max: belt[pointer] = - cell_max
        elif t == "-":
            belt[pointer] -= 1
            if belt[pointer] < -cell_max: belt[pointer] = cell_max
        elif t == ",":
            belt[pointer] = ord(input_text[input_pointer])
            input_pointer += 1
        elif t == ".":
            print(chr(belt[pointer]), end="")
        elif t == ">":
            pointer += 1
            if pointer >= len(belt): belt.append(0)
        elif t == "<":
            pointer -= 1
            if pointer == -1: debug_print(); raise IndexError("Belt has no index -1")
        elif t == "@":
            debug_print()
        else:
            while belt[pointer] != 0:
                parse(t)
        count += 1


def compile_brain_f(program_string, user_input):
    global belt
    global pointer
    global input_pointer
    global cell_max
    global input_text

    tokens = lexer(list(program_string), 0)

    belt = [0]
    pointer = 0
    input_pointer = 0
    cell_max = 300
    input_text = user_input

    print()
    parse(tokens)
