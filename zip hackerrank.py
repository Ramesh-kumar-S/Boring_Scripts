# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m=map(int,input().split())

res=[]

for i in range(int(m)):
    res.append(list(map(float,input().split())))

for i in zip(*res):
    print(sum(i)/m)