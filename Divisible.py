def solve (A):
    str1=''
    for i in range(0,len(A)//2):
        k=str(A[i])
        str1+= k[0]

    for j in range(len(A)//2,len(A)):
        str1+=str(A[j]%10)
    
    if int(str1) % 11==0:
        return "OUI"
    else:
        return "NON"
    # Write your code here

N = int(input())
A = [int(x) for x in input().split()]

out_ = solve(A)
print (out_)
