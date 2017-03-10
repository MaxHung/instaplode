def init(n):
	lst=[]
	for i in range(1,2**n):
		lst.append(0)
	return lst
def modify_l(l,i,x):
	if i ==0:
		l[1]=x
	else:
		l[(i+1)*2-1]=x
def modify_r(l,i,x):
	if i==0:
		l[2]=x
	else:
		l[(i+1)*2]=x
lst=init(4)
print lst #prints [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
modify_l(lst,5,10)
print lst #prints[0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,]
modify_r(lst,6,33)
print lst #prints [0,0,0,0,0,0,0,0,0,0,0,10,0,0,33]
