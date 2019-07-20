farrari=int(input())
car=0
for i in range(0,farrari):
  if(pow(2,i)>farrari):
    break
  car=farrari-pow(2,i)
print(car)
