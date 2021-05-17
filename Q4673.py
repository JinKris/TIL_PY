def d(n):
    sum = 0
    for i in list(str(n)):
        sum+=int(i)
    return sum + int(n)

dList = []

for i in range(1,10001):
    num = d(i)
    dList.append(num)

for i in range(1,10001):
    if i not in dList:
        print(i)