class Tree(object):
	def __init__(self, val, l=None, r=None):
		self.val = val
		self.l = l
		self.r = r
	def insert_l(self, a):
		self.l=Tree(a)
	def insert_r(self, b):
		self.r=Tree(b)
def travel(t):
	if t == None:
		return []
	return travel(t.l)+[t.val]+travel(t.r)
def build_Tree(n):
	if n <= 0 or type(n) != int:
		raise ValueError("Input should be whole number.")
	return [0]*(2**n)
def find_number(t, x):
	if x in travel(t):
		return True
	return False
