import requests

def captcha1(digitstring):
	digitstring = digitstring.strip()
	acc = 0
	prev = digitstring[-1]
	for c in digitstring:
		if c==prev:
			acc += int(c)
		prev = c
	return acc

assert captcha1('1122') == 3
assert captcha1('1111') == 4
assert captcha1('1234') == 0
assert captcha1('91212129') == 9

def captcha2(digitstring):
	digitstring = digitstring.strip()
	acc = 0
	for nr, c in enumerate(digitstring):
		if c == digitstring[(nr+len(digitstring)//2) % len(digitstring)]:
			acc += int(c)
	return acc

assert captcha2('1212') == 6
assert captcha2('1221') == 0
assert captcha2('123425') == 4
assert captcha2('123123') == 12
assert captcha2('12131415') == 4

cookie = {'session':'53616c7465645f5fe79e868af19f0f04a3c8d0cb27604d571e7ba19a1c85788b8f48b467f799a781a4e14e787a8a1dac'}
g = requests.get('http://adventofcode.com/2017/day/1/input', cookies=cookie)
print(g.text)
print(captcha1(g.text))
print(captcha2(g.text))

