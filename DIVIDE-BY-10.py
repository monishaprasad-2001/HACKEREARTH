N = int(input())
data = [int(x) for x in input().split()]
string = ''

for i in data:
    string+=str(i%10)

if int(string)%10==0:
    print("Yes")
else:
    print("No")
