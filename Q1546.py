num = int(input())
arr = list(map(int,input().split()))

arr.sort()

sum=0
for i in arr:
    sum+=i/arr[-1]*100
print(sum/num)