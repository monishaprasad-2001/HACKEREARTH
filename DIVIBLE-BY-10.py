
N = int(input())
data = [int(x) for x in input().split()]
arr = []
string = ''
for num in data:
    lastnum = (num%(len(str(num))*10))
    string = string + str(lastnum)

if int(string)%10==0:
    print("Yes")
else:
    print("No")
