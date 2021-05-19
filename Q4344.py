testNum = int(input());

for i in range(testNum):
    stuList=list(map(int,input().split()));
    stuNum=stuList[0];
    avg=sum(stuList[1:])/stuNum
    cnt = 0;
    for j in range(1,stuNum+1):
        if stuList[j]>avg:
            cnt+=1
    rate = float((cnt/stuNum)*100)
    print("%.3f%%"%rate)