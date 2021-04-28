from collections import Counter
n=int(input())
size=list(map(int,input().split()))
mylist=[]
ml1=[]
for i in range(int(input())):
    cussize,amt=list(map(int,input().split()))
    mylist.append(cussize)
    ml1.append(amt)
    
print(Counter(mylist))

sum=sum(ml1)