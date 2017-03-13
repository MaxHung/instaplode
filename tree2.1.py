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
	if t==None:
		return []
	else:
		lst=travel(t.l)+[t.val]+travel(t.r)
		return lst
def build_Tree(n):
	if n<=0 or type(n) != int:
		raise ValueError("Input should be whole number.")
	else:
		l=[]
		for i in range(1,2**(n)):
			l.append(i)
		return l
def find_number(t,x):
	if x in travel(t):
		return True
	return False
