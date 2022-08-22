def change_making(n, target, denominations):
    k=n
    def sub_problems(n, target):
        if n<0:
            return [1]*(k+1)
        if target<0:
            return [1]*(k+1)
        if target==0:
            return []
        else:
            change_one=sub_problems(n-1,target)
            change_two=sub_problems(n,target-denominations[n])+[denominations[n]]
            if len(change_one)<=len(change_two):
                return change_one
            else:
                return change_two
    return sub_problems(n,target)
denominations=[4,5,12,19]
target=16

denominations.sort(reverse=True)
print("lenngth of empty arrat", len([]), len([1,2,3]))
print("print final result", change_making(len(denominations)-1, target, denominations))
