def centered_average(nums):
	l = nums
	index = []
	value = []
	for i,j in enumerate(l):
	 	if j == 13:
			index.append(i+1)
		else:
			print sum(l)
	for i,j in enumerate(l):
		if i in index:
			value.append(j)
	for i in l:
    		if i in value:
        		l.remove(i)
	for i in l:
		if i == 13:
			l.remove(i)
			print sum(l)		
				
		
centered_average([1, 2, 2, 1, 13])
