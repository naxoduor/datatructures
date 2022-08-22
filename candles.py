def candies(n, arr):
    i=n
    count=0
    print("The value of n is",n)
    def give_candles(i,arr):
        print(i)
        if i==0:
            return 0
        print(arr[i-1], arr[i], arr[i+1], arr)
        if arr[i]>arr[i-1]:
            return 1+give_candles(i-1,arr)
        else:
            return 0

    return(give_candles(n, arr))

arr=[4,6,4,5,6,2]
n=len(arr)-2

print(candies(n,arr))