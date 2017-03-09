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
	if t==None:
		return []
	else:
		lst=lst+travel(t.l)+[t.val]+travel(t.r)
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
