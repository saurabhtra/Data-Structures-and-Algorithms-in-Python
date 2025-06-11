class MyStack(object):
    
    def __init__(self):
        self.item=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.item.append(x)
        for i in range(len(self.item)-1):
            self.item.append(self.item.pop(0))
        

    def pop(self):
        """
        :rtype: int
        """
        try:
            return self.item.pop(0)
        except:
            return -1
        

    def top(self):
        """
        :rtype: int
        """
        return self.item[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.item) ==0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.empty()

