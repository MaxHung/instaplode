def Tree(x,y=None,z=None):
    dict={}
    dict[x]=[y,z]
    return dict
print Tree(1) #returns {1: [None, None]}
print Tree(1,2,3) #returns {1: [2, 3]}
print Tree(1,Tree(1,2),Tree(1)) 
# returns {1: [{1: [2, None]}, {1: [None, None]}]}