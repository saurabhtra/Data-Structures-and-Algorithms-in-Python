class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        maxi = max(deadline)
        arr=[-1]*maxi
        print(arr)
        print(sum(profit))
        mylist =[(deadline[i]-1,profit[i]) for i in range(len(profit))]
        mylist.sort(key=lambda x:x[1],reverse=True)
        print(mylist)
        maxpro = 0
        count =0 
        for i in range(len(profit)):
            if arr[mylist[i][0]] == -1:
                arr[mylist[i][0]] = 1
                count+=1
                print("adding",mylist[i][1] )
                maxpro+=mylist[i][1]
            else:
                j =mylist[i][0]-1
                while j >=0:
                    if arr[j] ==-1:
                        arr[j] =1
                        count+=1
                        maxpro+=mylist[i][1]
                        break
                    j -=1
        print([count,maxpro])
                
            
dommy =Solution()


dommy.jobSequencing(deadline = [11 ,2, 5, 8, 11 ,10, 1, 6, 3, 8, 10], profit = [321, 62 ,456 ,394 ,424 ,22, 393, 87, 118, 384, 83])