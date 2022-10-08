# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>0 and y>0:
        if x==y:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")