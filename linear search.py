num=list(map(int,input("enter number:").split()))
search=int(input("enter searching number:"))
x=-1
for i in range(len(num)):
    if num[i]==search:
        x=i
        break
    
    
if x==-1:
    print("not found")
else:
    print("item found in {} position".format(x))