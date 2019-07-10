doo3=input()
san=0
for n in range(len(doo3)):
  if(doo3[n].isdigit() or doo3[n].isalpha() or doo3[n]==(" ")):
    continue
  else:
   san+=1
print(san)
