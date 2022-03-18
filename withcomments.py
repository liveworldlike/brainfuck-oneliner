(lambda interpreter_function,       # Interpreter function for recursive callse
        program_tape,               # Program to be interpreted
        memory_pointer,             # Pointer to the current position in the memory tape
        memory_tape,                # Array of integers, representing the memory tape
        input_tape,                 # Tape with input characters, representer by array of chars
                                    # If there are no characters in the input tape, a line from stdin is read
        instruction_pointer:        # A pointer to the current instruction in the program tape
    memory_pointer if (instruction_pointer >= len(program_tape) or program_tape[instruction_pointer] not in '<>+-.,[]') else
    {
        # Practically for every instruction, instruction pointer is increased
        # Interpreter call should return the new memory pointer to allow loops to be processed
        # The elements in the dictionary are lambda functions to prevent the call to the functions during dictionary instantiation
        '>': lambda: interpreter_function(interpreter_function, program_tape, memory_pointer + 1, memory_tape, input_tape, instruction_pointer + 1),
        '<': lambda: interpreter_function(interpreter_function, program_tape, memory_pointer - 1, memory_tape, input_tape, instruction_pointer + 1),
        '+': lambda: (memory_tape.insert(memory_pointer, memory_tape.pop(memory_pointer) + 1), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[1],
        '-': lambda: (memory_tape.insert(memory_pointer, memory_tape.pop(memory_pointer) - 1), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[1],
        '.': lambda: (print(chr(memory_tape[memory_pointer]), end=''), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[1],
        ',': lambda: (memory_tape.pop(memory_pointer), memory_tape.insert(memory_pointer, ord(input_tape.pop(0)) if input_tape else (input_tape.extend(list(input())), ord(input_tape.pop(0)))[1]), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[2],
        '[': lambda: interpreter_function(interpreter_function, program_tape, interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1), memory_tape, input_tape, instruction_pointer) if memory_tape[memory_pointer] else interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape,
                        # Calculates the position of the closing parenthesis(']'), by performing the following:
                        # Constructs new array: if the number of opening parenthesis matches the number of closing
                        # parenthesis before certain instruction in program, assign the number of this instruction
                        # to the corresponding array cell, otherwise assigns the len of the program
                        # Then, the minimum over the array is chosen as the next instruction to be executed (after the loop ended)
                        min([len(program_tape) if (program_tape[instruction_pointer:j].count('[') != program_tape[instruction_pointer:j].count(']')) else j for j in range(instruction_pointer + 1, len(program_tape))])
                    ),
        ']': lambda: memory_pointer,
    }[program_tape[instruction_pointer]]())((lambda interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer:
    memory_pointer if (instruction_pointer >= len(program_tape) or program_tape[instruction_pointer] not in '<>+-.,[]') else\
    {
        '>': lambda: interpreter_function(interpreter_function, program_tape, memory_pointer + 1, memory_tape, input_tape, instruction_pointer + 1),
        '<': lambda: interpreter_function(interpreter_function, program_tape, memory_pointer - 1, memory_tape, input_tape, instruction_pointer + 1),
        '+': lambda: (memory_tape.insert(memory_pointer, memory_tape.pop(memory_pointer) + 1), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[1],
        '-': lambda: (memory_tape.insert(memory_pointer, memory_tape.pop(memory_pointer) - 1), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[1],
        '.': lambda: (print(chr(memory_tape[memory_pointer]), end=''), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[1],
        ',': lambda: (memory_tape.pop(memory_pointer), memory_tape.insert(memory_pointer, ord(input_tape.pop(0)) if input_tape else (input_tape.extend(list(input())), ord(input_tape.pop(0)))[1]), interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1))[2],
        '[': lambda: interpreter_function(interpreter_function, program_tape, interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, instruction_pointer + 1), memory_tape, input_tape, instruction_pointer) if memory_tape[memory_pointer] else interpreter_function(interpreter_function, program_tape, memory_pointer, memory_tape, input_tape, min([len(program_tape) if (program_tape[instruction_pointer:j].count('[') != program_tape[instruction_pointer:j].count(']')) else j for j in range(instruction_pointer + 1, len(program_tape))])),
        ']': lambda: memory_pointer,
    }[program_tape[instruction_pointer]]()), input(), 0, [0] * 100000, [], 0)
    # The function is called with itself as an interpreter, zeroes as memory and instruction pointers,
    # one line from stdin as input tape, and array of 10^5 zeroes as memory tape