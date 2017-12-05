import requests

def isvalid(phrase):
	seen = set()
	for word in phrase.split():
		if word in seen:
			return False
		seen.add(word)
	return True

assert isvalid('aa bb cc dd ee') 
assert not isvalid('aa bb cc dd aa') 
assert isvalid('aa bb cc dd aaa') 

def isvalid2(phrase):
	seen = set()
	for word in phrase.split():
		anagram = ''.join(sorted(word))
		if anagram in seen:
			return False
		seen.add(anagram)
	return True

assert isvalid2('abcde fghij') 
assert not isvalid2('abcde xyz ecdab') 
assert isvalid2('a ab abc abd abf abj') 
assert isvalid2('iiii oiii ooii oooi oooo') 
assert not isvalid2('oiii ioii iioi iiio') 


cookie = {'session':'53616c7465645f5fe79e868af19f0f04a3c8d0cb27604d571e7ba19a1c85788b8f48b467f799a781a4e14e787a8a1dac'}
g = requests.get('http://adventofcode.com/2017/day/4/input', cookies=cookie)
# print(g.text)
print(len([1 for phrase in g.text.strip().split('\n') if isvalid(phrase)]))
print(len([1 for phrase in g.text.strip().split('\n') if isvalid2(phrase)]))
