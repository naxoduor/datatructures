def getWays(c, n):
    i=len(c)-1
    cach={}
    def sub_problems(i, n):
        if (i,n) in cach:
            return cach[(i,n)]
        if c[i]>n:
            choice_take=0
        elif c[i]==n:
            choice_take=1
        else:
            choice_take=sub_problems(i, n-c[i])
        if i==0:
            choice_leave=0
        else:
            choice_leave=sub_problems(i-1, n)
        total_ways = choice_take+choice_leave
        cach[(i,n)]=total_ways
        return total_ways
    return sub_problems(i, n)


c=[2,5,3,6]
n=10

print(getWays(c, n))
