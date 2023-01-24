# cook your dish here
a= int(input())
for i in range(a):
    n = int(input())
    S = list(map(int, input().split()))
    S.sort()
    mini=99999999999
    for i in range(n-1):
        diff= abs(S[i+1] - S[i])
        if diff<mini:
            mini= diff  
    print(mini)  
