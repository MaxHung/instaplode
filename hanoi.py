def Hanoi(n):
	if n == 1:
		return 1
	return Hanoi(n-1)+2**(n-1)
print Hanoi(3)#7
print Hanoi(4)#15
print Hanoi(999)# Huge number