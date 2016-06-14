def tralling_factorial(num):
	factorial = 1
	if num > 0:
		for i in range(1,num+1):
			factorial = factorial * i
			if(i == num):
				l = [factorial]
				k = map(int,str(factorial))
				for i,j in enumerate(k[::-1]):
					if j > 0:
						print i
						break
	else:
		print "number greater than zero"
tralling_factorial(999)	