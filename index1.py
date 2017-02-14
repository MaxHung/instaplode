lst=[1,2,3,4,5,6,7,8,9,10,55]
def fi(l,n):
    mn=0
    mx=len(l)-1
    i=int((len(l)-1)/2)+1
    while l[i]!=n:
        if l[i]>n:
            mx=i
            i=int((mx+mn)/2)
        elif l[i]<n:
            mn=i
            i=int((mx+mn)/2)+1
    print i
print fi(lst,10)