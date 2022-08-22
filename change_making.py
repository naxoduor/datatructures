def change_making(n, target, denominations):
    def sub_problems(n, target):
        if denominations[n]>target:
            choice_take=float('inf')
        elif target==denominations[n]:
            print('print denomination', denominations[n])
            choice_take=1
        else:
            choice_take=1+sub_problems(n, target-denominations[n])
        if n==0:
            choice_leave=float('inf')
        else:
            choice_leave=sub_problems(n-1, target)
        optimal=min(choice_take, choice_leave)
        print("print optimal",optimal)
        return optimal
    return sub_problems(n,target)

denominations=[1,5,12,19]
target=16

print(change_making(len(denominations)-1, target, denominations))

