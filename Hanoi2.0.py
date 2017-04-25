def Hanoi(n,start=1,turn=2,end=3):
	if n == 1:
		print "%s --> %s" %(start,end)
	else:
		Hanoi(n-1,start,end,turn)
		print "%s --> %s" %(start,end)
		Hanoi(n-1,turn,start,end)
