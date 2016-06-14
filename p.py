# find the all the possible prime number from the given integer number

from itertools import permutations

number = 3657
strNumber = str(number)
listNumbers = []

def is_prime(a):
    return all(a % i for i in xrange(2, a))

for i in xrange(1, len(strNumber)+1):
	_list = map(lambda n: int("".join(n)), permutations(strNumber, i))
	listNumbers.extend(_list)
listNumbers = list(set(listNumbers))

for n in listNumbers:
	if is_prime(n):
		print n,