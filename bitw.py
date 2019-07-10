lov1,lov2=map(int,input().split())
lov1=lov1*lov2
lov2=lov1//lov2
lov1=lov1//lov2
print(lov1,lov2)
