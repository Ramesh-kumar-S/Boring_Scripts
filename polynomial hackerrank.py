# Enter your code here. Read input from STDIN. Print output to STDOUT


def evaluator(x,k,eqn):
    xs=[ x.strip() for x in eqn.split('+') ]
    sum=0
    for i in xs:
        sum += eval(i)
    if sum==k:
        print("True")
    else:
        print("False")
        
   
        
x,k=map(int,input().split())
eqn=input()

evaluator(x,k,eqn)