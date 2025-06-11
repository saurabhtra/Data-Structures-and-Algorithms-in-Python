def mergeInterval(intervals):
    tobemergerd = []
    for i in range(len(intervals)-1):
        for j in range(i+1,len(intervals)):
            if intervals[i][1] > intervals[j][0]:
                tobemergerd.append([i,j])
    ans=[]
    
    for arr in tobemergerd:
        
        ans.append([intervals[arr[0]][0],intervals[arr[1]][1]])
    return ans
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()

# print(mergeInterval(intervals))
ans = [intervals[0]] #[[1,3]]
i = 0 #pointer to ans
j = 1
# while j < len(intervals):
#     if ans[i][1] > intervals[j][0]:
#         ans[i][1] = intervals[j][1]
#         j+=1
#     else:
#         ans.append(intervals[j])
#         i+=1
#         j+=1

# print(ans)
# intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = [intervals[0]] #[[1,3]]
for arr in intervals:
    if ans[-1][1] >= arr[0]:
        print("ans[-1][0] = " ,ans[-1][0])
        ans[-1][1] = max(arr[1],ans[-1][-1])
    else:
        ans.append(arr)
print(ans)



