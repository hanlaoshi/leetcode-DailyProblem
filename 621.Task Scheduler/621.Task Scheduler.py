---------------------------------辰星出品----------------------------
# encoding: utf-8
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """        
        DictTask = {}        
        for task in tasks:
            DictTask[task] = DictTask.get(task, 0) + 1
        if n == 0:
            return len(tasks)

        def defaultStackDictAdd(default_dict, key, item):
            if key not in default_dict:
                default_dict[key] = [item]
            else:
                default_dict[key].append(item)

        DictCnt = {}    
        for task, cnt in DictTask.items():
            defaultStackDictAdd(DictCnt, cnt, task)

        self.ListQueue = [None] * n
        self.PosiQueue = 0
        self.CntTaskInQueue = 0
        self.CntProcessedTask = 0

        def putQueue(dictn, task, nums):                    
            if self.ListQueue[self.PosiQueue] != None:
                LastTask, cnt = self.ListQueue[self.PosiQueue]
                defaultStackDictAdd(dictn, cnt, LastTask)
                self.CntTaskInQueue -= 1
            if task == None or nums <= 1:
                self.ListQueue[self.PosiQueue] = None
            else:
                self.ListQueue[self.PosiQueue] = (task, nums - 1)
                self.CntTaskInQueue += 1
            self.CntProcessedTask += 1
            self.PosiQueue += 1
            if self.PosiQueue >= n:
                self.PosiQueue = 0

        while DictCnt or self.CntTaskInQueue:
            if DictCnt:
                MaxKey = max(DictCnt.keys())
                putQueue(DictCnt, DictCnt[MaxKey].pop(), MaxKey)
                if not DictCnt[MaxKey]:
                    DictCnt.pop(MaxKey)
            else:
                putQueue(DictCnt, None, 0)
        return self.CntProcessedTask
if __name__ == "__main__":

    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(Solution().leastInterval(tasks, n))
-------------------------------解法2------------------------------
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] = output[ord(i)-ord('A')]+1
 
        count = 0
        len_o = 0
        max_o = max(output)
        for i in output:
            if i==max_o:
                count = count+1
                    
        return max(len(tasks),(max_o-1)*(n+1)+count) 
