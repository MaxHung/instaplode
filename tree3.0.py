def init(n):
	return [0]*(2**n)
def modify_l(l,i,x):
		l[i*2+1]=x
def modify_r(l,i,x):
		l[(i+1)*2]=x
lst=init(4)
print lst #prints [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
modify_l(lst,5,10)
print lst #prints[0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,]
modify_r(lst,6,33)
print lst #prints [0,0,0,0,0,0,0,0,0,0,0,10,0,0,33]
