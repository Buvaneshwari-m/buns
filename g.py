hide=int(input())
t,r=0,1
while hide>0:
  print(r,end=' ')
  t,r=r,t+r
  hide=hide-1
