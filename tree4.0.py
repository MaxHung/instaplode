class Tree(object):
	def __init__(self,val,l=None, r=None):
		self.val=val
		self.l=l
		self.r=r
	def insert(self,x):
			if x< self.val:
				if type(self.l) == int or self.l==None:
					self.l= Tree(x)
				else:
					self.l.insert(x)
			else:
				if type(self.r) == int or self.r==None:
					self.r=Tree(x)
				else:
					self.r.insert(x)
	def travel(self):
		if self.l==None:
			left=[]
		else:
			left=self.l.travel()
		if self.r==None:
			right=[]
		else:
			right=self.r.travel()
		lst=left+[self.val]+right
		return lst
def sort_list(l):
	t=Tree(l[0])
	for i in range(1,len(l)):
		t.insert(l[i])
	return t.travel()
print sort_list([9,8,7,6,5,4,3,2,1]) #returns [1,2,3,4,5,6,7,8,9]