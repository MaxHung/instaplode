def fibo(n):
	if n <= 0:
		return False
	elif n==1:
		return 1
	elif n==2:
		return 1
	else:
		return (fibo(n-2)+fibo(n-1))
print fibo(5) #This returns 5
print fibo(7) #This returns 7
print fibo(10) #This returns 55