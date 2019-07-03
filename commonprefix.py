#sharmila
n=int(input())
in1=[]
in2=[]
for i in range(0,n):
  in1.append(input())
for i in in1:
  in2.append(len(i))
j1=0
for i in range(0,min(in2)):
  for j in range(1,n):
    if in1[0][i]==in1[j][i]:
      j1=0
    else:
      j1=1
      break
  if j1==0:
    print(in1[0][i],end='')
