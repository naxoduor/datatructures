def candies(n, arr):
    i=n
    count=0
    print("The value of n is",n)
    def give_candles(i,arr):
        print("print i", i)
        if i==0:
            return 0
        if i==n+1:
            return 0
        print("The candles are as shown below", i,n)  
        return give_candles(i-1, arr)  
        # return min(give_candles(i-1, arr), give_candles(i+1, arr))

        # print("The candles are as shown below", arr[i-1], arr[i], arr[i+1])
        # if arr[i-1]<arr[i] and arr[i]<arr[i+1]:
        #     print("middle max found")
        #     return min(give_candles(i-1, arr), give_candles(i+1, arr))
        # # if arr[i-1]<arr[i]:
        #     return 1+give_candles(i-1, arr)
        # else:
        #     return give_candles(i-1, arr)
    return(give_candles(n, arr))

arr=[4,6,4,5,6,2]
n=len(arr)-1

print("The candles counted are",candies(n,arr))