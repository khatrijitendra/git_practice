def decent_number():
	l1 = []
	t = int(raw_input())
	for i in range(t):
		y=int(raw_input()) 
		z = y 
		while(z%3!=0): 
			z-=5 
		if(z<0): 
			l1.append('-1') 
		else: 
			l1.append(z*'5'+(y-z)*'3')
	for i in l1:		
		print i		

decent_number()