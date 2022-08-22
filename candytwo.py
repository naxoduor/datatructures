def candies(n, arr):
    i=n
    count=0
    print("The value of n is",n)
    def give_candles(i,arr):
        print("print i", i)
        if i==0:
            return 0
        elif i==n+1:
            return 0
        else:
            return min(give_candles(i-1, arr), give_candles(i+1, arr))
    return(give_candles(n, arr))

arr=[4,6,4,5,6,2]
n=len(arr)-1

print("The candles counted are",candies(n,arr))