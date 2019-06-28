q,t4=map(int,input().split())
if(t4<=100000):
  for x in range(q+1,t4):
    if(x%2!=0):
      print(x,end=" ")
