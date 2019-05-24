#------------deque实现。-------------------
from collections import deque
class RecentCounter:
    def __init__(self):
        self.pings = deque()        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        while self.pings[0] < t - 3000:
            self.pings.popleft()
        return len(self.pings)

		
#-------------二分搜索发优化搜索过程------------------------
class RecentCounter:
    def __init__(self):
        self.pings = list()       

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        l, r = 0, len(self.pings)
        if t > 3000:
            while l < r:
                mid = (l + r)//2
                if self.pings[mid] < t - 3000:
                    l = mid + 1
                else:
                    r = mid
            
        return len(self.pings) - l
