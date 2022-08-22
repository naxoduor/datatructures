def change_making(n, target, denominations):
    arr_one=[]
    arr_two=[]
    def sub_problems(n, target):
        if n<0:
            return float('inf')
        if target<0:
            return float('inf')
        if target==0:
            return 0
        else:
            change_one=sub_problems(n-1, target)
            change_two=1+sub_problems(n,target-denominations[n])
            return min(change_one, change_two)
    return sub_problems(n,target)

denominations=[4,5,12,19]
target=16

denominations.sort(reverse=True)
print(change_making(len(denominations)-1, target, denominations))
