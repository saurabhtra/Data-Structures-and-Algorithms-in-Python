#User function Template for python3
start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        mytuple = [(start[i],end[i])for i in range(len(start))]
        mytuple.sort(key=lambda x:(x[1],x[0]))
        result =[]
        count =1
        result.append(mytuple[0])
        lastend =mytuple[0][1]
        for i in range(len(start)):
            if mytuple[i][0] > lastend:
                result.append(mytuple[i])
                lastend = mytuple[i][1]
                count+=1
        print(result)
        return count
dommy=Solution()
print(dommy.maximumMeetings(start,end))