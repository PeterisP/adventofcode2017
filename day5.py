import requests
import numpy as np

def jumps(offsets):
	matrix = np.array(offsets, dtype=np.int32)
	steps = 0
	pointer = 0
	while True:
		offset = matrix[pointer]
		matrix[pointer] = offset + 1
		pointer = pointer + offset
		steps += 1
		if pointer<0 or pointer >=len(matrix):					
			return steps

assert jumps([0, 3, 0, 1, -3]) == 5

def jumps2(offsets):
	matrix = np.array(offsets, dtype=np.int32)
	steps = 0
	pointer = 0
	while True:
		offset = matrix[pointer]
		if offset<3:
			matrix[pointer] = offset + 1
		else:
			matrix[pointer] = offset - 1
		pointer = pointer + offset
		steps += 1
		if pointer<0 or pointer >=len(matrix):					
			return steps

assert jumps2([0, 3, 0, 1, -3]) == 10

cookie = {'session':'53616c7465645f5fe79e868af19f0f04a3c8d0cb27604d571e7ba19a1c85788b8f48b467f799a781a4e14e787a8a1dac'}
g = requests.get('http://adventofcode.com/2017/day/5/input', cookies=cookie)
print(jumps([int(x) for x in g.text.strip().split('\n')]))
print(jumps2([int(x) for x in g.text.strip().split('\n')]))
