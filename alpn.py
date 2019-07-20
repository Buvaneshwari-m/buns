exotic=input()
count1=0
for go1 in exotic:
  if (go1.isdigit() or go1.isalpha()):
    count1+=1
if count1!=0:
  print("Yes")
else:
  print("No")
