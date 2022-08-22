def change_making(n, target, denominations):
    def sub_problems(n, target):
        if denominations[n]>target:
            return float('inf')
        elif target==denominations[n]:
            return 1
        elif n==0:
            return float('inf')
        else:
            return min(1+sub_problems(n, target-denominations[n]), sub_problems(n-1, target))
    return sub_problems(n,target)

denominations=[1,5,12,19]
target=16

print(change_making(len(denominations)-1, target, denominations))

