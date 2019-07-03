#sharmila
n=int(input())
in1=[]
for i in range(0,n):
  in1.append(input())
for i in range(0,len(min(in1))):
  if in1[0][i]==in1[1][i]:
    print(in1[0][i],end='')
  else:
    break
