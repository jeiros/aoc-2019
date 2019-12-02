def process_program(program_str):
	return list(map(int, program_str.split(",")))

def solve_program(program):
	i = 0  # Cursor
	while program[i] != 99:  # Halt
		loc1, loc2, loc3 = program[i+1], program[i+2], program[i+3]
		if program[i] == 1: # Summation
			program[loc3] = program[loc1] + program[loc2]
		elif program[i] == 2:  # Multiplication
			program[loc3] = program[loc1] * program[loc2]
		else:
			raise RunTimeError("Code {} not allowed.".format(program[i]))
		i += 4  # Move to next Opcode
	return program


def compute_output(noun, verb, program):
	program[1] = noun
	program[2] = verb
	return solve_program(program)[0]


assert solve_program(process_program("1,0,0,0,99")) == [2,0,0,0,99]
assert solve_program(process_program("2,3,0,3,99")) == [2,3,0,6,99]
assert solve_program(process_program("2,4,4,5,99,0")) == [2,4,4,5,99,9801]
assert solve_program(process_program("1,1,1,4,99,5,6,0,99")) == [30,1,1,4,2,5,6,0,99]

if __name__ == '__main__':
	# Part 1
	input1 = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0'
	program_initial = process_program(input1)
	# Restore state
	program_initial[1] = 12
	program_initial[2] = 2
	print("Part 1", solve_program(program_initial)[0])

	# Part 2
	for noun in range(100):
		for verb in range(100):
			if compute_output(noun, verb, process_program(input1)) == 19690720:
				print("Match found: ", 100 * noun + verb)
				break
