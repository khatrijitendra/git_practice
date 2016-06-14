def reversed_string():
	l = int(raw_input("enter number of test cases -->  "))
	i = 0
	li = []
	while(i < l):
		s = raw_input("enter strings -->  ")			
		li.append(s)
		i += 1	
	for e in li:
		print e[::-1]

reversed_string()