import requests
from itertools import permutations

sample_data = [[5,1,9,5], [7,5,3], [2,4,6,8]]
sample_data2 = [[5,9,2,8], [9,4,7,3], [3,8,6,5]]

def checksum(spreadsheet):
	acc = 0
	for row in spreadsheet:
		acc += max(row) - min(row)
	return acc


def checksum2(spreadsheet):
	acc = 0
	for row in spreadsheet:
		for (a,b) in permutations(row,2):
			if a % b == 0:
				acc += a // b

	return acc

assert checksum(sample_data) == 18
assert checksum2(sample_data2) == 9


cookie = {'session':'53616c7465645f5fe79e868af19f0f04a3c8d0cb27604d571e7ba19a1c85788b8f48b467f799a781a4e14e787a8a1dac'}
g = requests.get('http://adventofcode.com/2017/day/2/input', cookies=cookie)
data = [[int(y) for y in x.split()] for x in g.text.strip().split('\n')]
print(data)
print(checksum(data))
print(checksum2(data))
