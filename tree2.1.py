class Tree(object):
	def __init__(self,val,l=None,r=None):
		self.val=val
		self.l=l
		self.r=r
	def insert_l(self,a):
		self.l=Tree(a)
	def insert_r(self,b):
	    self.r=Tree(b)
def travel(t):
	lst=[]
	c=0
	if t==None:
		return [None]
	elif type(t) == int:
		return [t]
	else:
		lst=lst+travel(t.l)+travel(t.val)+travel(t.r)
		for i in lst:
			if i==None:
				c=c+1
		for n in range(0,c):
			lst.remove(None)
		return lst
	return lst
def build_Tree(n):
	if n<=0 or type(n) != int:
		raise ValueError("Input should be whole number.")
	else:
		l=[]
		for i in range(1,2**(n)):
			l.append(i)
		return l
a=Tree(0)
a.insert_l(1)
print travel(a)
print build_Tree(4)
