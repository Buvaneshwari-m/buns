das=input()
cnt=0
for p in range(0,len(das)):
    if(das[p].isdigit() or das[p].isalpha() or das[p]==' '):
        continue
    else:
        cnt=cnt+1
print(cnt)
