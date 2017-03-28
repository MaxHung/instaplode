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
def build_tree(l):
	t = Tree(l[0])
	i = 0
	lst=[t]
	while i <= len(l) - 1:
		if i + 1 <= len(l) - 1 and l[i+1] != None:
			left = Tree(l[i+1])
			lst[0].l = left
			lst.append(left)
		if i +2 <= len(l) - 1 and l[i+2] != None:
			right = Tree(l[i+2])
			lst[0].r = right
			lst.append(right)
		i = i + 2
		lst.pop(0)
	return t