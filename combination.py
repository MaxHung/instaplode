def combination(m,n):
	if m < n:
		raise ValueError("m cannot be less than n")
	elif m == n or n == 0:
		return 1
	else:
		return combination(m-1,n-1)+combination(m-1,n)
print combination(10,5) #prints 252