import itertools
import numpy as np
data = 347991

def steps_old(nr):
	if nr==1:
		return 0
	for radius in itertools.count():
		end = (radius*2 + 1) ** 2
		if end >= nr:
			break
	pos_on_line = (nr - (radius*2-1)**2) % (radius*2)
	steps = radius + abs(radius-pos_on_line)
	print(nr, radius, pos_on_line, steps)
	return steps


def steps(nr):
	x = 0
	y = 0
	matrix = np.zeros((1000,1000), dtype=np.int32)
	matrix[x+500, y+500] = 1
	direction = 'left'
	for i in range(nr-1):
		if direction == 'left':
			x = x+1
			if matrix[x+500, y+501] == 0:
				direction = 'up'
		elif direction == 'up':
			y = y+1
			if matrix[x+499, y+500] == 0:
				direction = 'right'
		elif direction == 'right':
			x = x-1
			if matrix[x+500, y+499] == 0:
				direction = 'down'
		elif direction == 'down':
			y = y-1
			if matrix[x+501, y+500] == 0:
				direction = 'left'
		else:
			print(direction)
			assert False
		value = matrix[x+499, y+499] + matrix[x+499, y+500] + matrix[x+499, y+501] + matrix[x+500, y+499] + matrix[x+500, y+501] + matrix[x+501, y+499] + matrix[x+501, y+500] + matrix[x+501, y+501]
		matrix[x+500, y+500] = value
		if value > 347991:
			print(i+2, x, y, value)
			break
	return abs(x)+abs(y)

# assert steps(1) == 0
# assert steps(2) == 1
# assert steps(3) == 2
# assert steps(6) == 1
# assert steps(9) == 2
# assert steps(12) == 3
# assert steps(23) == 2
# assert steps(25) == 4
# assert steps(1024) == 31

print(steps(data))

