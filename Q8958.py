num = int(input())

for i in range(num):
    arr=input()
    score=0
    result=0
    for j in arr:
        if j=='O':
            score+=1
            result+=score
        else:
            score=0
    print(result)
