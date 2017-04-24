def Hanoi(n,start=1,turn=2,end=3):
	if n == 1:
		print "%s --> %s" %(start,end)
	elif n == 2:
		print "%s --> %s" %(start,turn)
		print "%s --> %s" %(start,end)
		print "%s --> %s" %(turn,end)
	elif n == 3:
		print "%s --> %s" %(start,end)
		print "%s --> %s" %(start,turn)
		print "%s --> %s" %(end,turn)
		print "%s --> %s" %(start,end)
		print "%s --> %s" %(turn,start)
		print "%s --> %s" %(turn,end)
		print "%s --> %s" %(start,end)
	else:
		Hanoi(n-1,start,end,turn)
		print "%s --> %s" %(start,end)
		Hanoi(n-1,turn,start,end)