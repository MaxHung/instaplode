class Tree(object):
	def __init__(self, val, l=None, r=None):
		self.val = val
		self.l = l
		self.r = r
	def insert_l(self, a):
		self.l = Tree(a)
	def insert_r(self, b):
		self.r = Tree(b)
def search(t):
	lst = [t]
	while len(lst) != 0:
		i = lst[0]
		if i.l != None:
			lst.append(i.l)
		if i.r != None:
			lst.append(i.r)
		lst[0] = i.val
		print i.val
		lst.pop(0)
def build_tree(l):#does not work
	t=Tree(l[0])
	lst=[t]
	for i in range(0, len(l)):
		if l[i] != None:
			lst[0] = Tree(l[i])
			lst.append((lst[0]).l)
			lst.append((lst[0]).r)
			print lst[0]
		lst.pop(0)
a = Tree(1)
a.insert_l(2)
a.insert_r(3)
a.l.insert_r(4)
search(a)
