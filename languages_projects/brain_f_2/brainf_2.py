from languages_projects.brain_f_2.brain_f_parser import compile_brain_f

file_location = "languages_projects/brain_f_2/brainf_2.txt"

# use the code written in brain_f_2.txt to create and manipulate functions
program_file = open(file_location, "r")
code_lines = program_file.readlines()
program_file.close()

# input for the program
program_file = open("languages_projects/brain_f_2/brain_f_2_input.txt", "r")
input_text = list("".join(program_file.readlines()))
program_file.close()

# the collection of all the compiled code
compiled_text = ""


#
# ------------------------- IMPORTANT VARIABLES -------------------------
#
current_position = 0
belt_len = 0


# a raw function, like ">[-]+>>", that is pure brain_f
class RawFunc:
    def __init__(self, operations):
        self.operations = operations


# the general structure of all brain_f_2 functions
class Function:
    def __init__(self, cells_used, operations):
        self.cells_used = cells_used
        self.operations = operations

    def run_operations(self):
        global compiled_text
        compiled_text += self.operations


# a simple comparison function structure
class ComparisonFunction(Function):
    def __init__(self, cells_used, operations, parameters, inputs_loc, outputs_loc):
        super().__init__(cells_used, operations)
        self.parameters = parameters
        self.inputs_loc = inputs_loc
        self.outputs_loc = outputs_loc

    def set_parameters(self):
        global compiled_text
        compiled_text += self.parameters

    def get_inputs_loc(self):
        return self.inputs_loc

    def get_outputs_loc(self):
        return self.outputs_loc


# simple functions
def move(x):
    global current_position
    current_position += x

    if x > 0:
        return x * ">"
    else:
        return x * "<"


def add(x):
    if x > 0:
        return x * "+"
    else:
        return x * "-"


def goto(x):
    global current_position
    new_pos = move(x - current_position)

    current_position = x
    return new_pos


def shift(a, b):
    return goto(a) + f"[-{goto(b)}+{goto(a)}]"


def set_char(c):
    return "[-]" + add(ord("H"))


def print_c():
    return "."


def append(text):
    global compiled_text
    compiled_text += text


# defining if zero
if_zero = ComparisonFunction(
    3,
    RawFunc("[[-]->]>[<]<+"),
    RawFunc(">>[-]+<<"),
    [0],
    [0]
)


# ------------------------- the part that actually does the brain_f stuff -------------------------
append(
set_char("H") + print_c() +
set_char("e") + print_c() +
set_char("l") + print_c() +
set_char("l") + print_c() +
set_char("o") + print_c()
)








# run the compiled code
print(compiled_text)
compile_brain_f(compiled_text, input_text)
