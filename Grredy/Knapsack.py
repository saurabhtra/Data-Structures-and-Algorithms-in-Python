def fractionalknapsack( val, wt,cap):
    #code here
    arr=[]
    for i in range(len(val)):
        arr.append([val[i],wt[i]])
    arr.sort(key=lambda x:x[0]/x[1],reverse=True)
    print(arr)
    currw=0.0
    tval=0.000000
    for i in range(len(arr)):
        if currw+arr[i][1] <=cap:
            currw+=arr[i][1]
            tval+=arr[i][0]
        else:
            rem = cap-currw
            tval+=float((arr[i][0]/arr[i][1])*rem)

            break
    return tval



val = [60, 100, 120]
wt = [10, 20, 30]
capacity=50
print(fractionalknapsack(val,wt,capacity))

            