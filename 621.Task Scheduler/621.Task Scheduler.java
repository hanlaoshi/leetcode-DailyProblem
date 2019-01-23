解法：【贪心 + 数学表达】

【贪心算法】角度的选择很重要。作者在这里采取了分块的形式，按照出现频率最多（假设频率为k）的将其分为了k块，然后每一轮向这k个区间个插入1个。如何选择贪心策略？
【数学公式表达】通过数学公式明确考虑问题的角度，清晰表达解答问题的思路，明确其中涉及的变量以及变量函数间的关系。
【证明贪心有效性】如何证明一个贪心策略是能够解决一个问题的？
// (c[25] - 1) * (n + 1) + 25 - i  is frame size
// when inserting chars, the frame might be "burst", then tasks.length takes precedence
// when 25 - i > n, the frame is already full at construction, the following is still valid.
public class Solution {
    public int leastInterval(char[] tasks, int n) {
 
        int[] c = new int[26];
        for(char t : tasks){
            c[t - 'A']++;
        }
        Arrays.sort(c);
        int i = 25;
        while(i >= 0 && c[i] == c[25]) i--;
 
        return Math.max(tasks.length, (c[25] - 1) * (n + 1) + 25 - i);
    }
}
------------------------2-----------------------
 总结了一下，LeetCode上的达人们的思路主要有这样几种：

1、先统计词频，再排序，从后往前找到第一个不是最大词频的下标i，结果是tasks.length或(c[25] - 1) * (n + 1) + 25 – i中大的那一个，25-i就是最大词频的任务类，这个和我的思路是一样的。
证明：最大词频是k，则创建k个块，每一块开头是最大词频的任务构成的(输入AACCCDDEEE，则开头是CE)，词频由大到小插入每一块。97.69%，10ms。

2、贪心，利用优先队列排序：队列中保存<类型，个数>的map，并且按照个数由大到小排序。按照词频由大到小取出n+1个或者队列中全部(若没有取出全部，则总长度要加上空闲个数)，
再把词频-1之后不为0的放回队列中。直到队列空了为止。——其实也和前面相同，总是选择词频最大的填入每一块。

3、使用操作系统的思想，在时间为time的时候，把time-1-n冻结的任务放回等待队列waitingQueue，在一个循环结束的时候，如果还有这一类task待完成，放到tasksTable。
具体做法：先用HashMap统计词频，再用优先队列waitingQueue排序，声明一个冷却HashMap表coolDownTable，当队列不空或者冷却表不空的时候，找到冷却表time-n-1对应的任务char，
拿出放到等待队列中，如果等待队列不空{拿出任务，剩余任务个数-1并放到tasksTable，如果剩余任务个数不为0放到coolDownTable.put(time, task); } time++。返回time

4、类似上面，模拟的思想：对于m个任务，先是每类任务的冷却时间-1，然后找到词频最大的任务及其下标，如果它的词频>-1，则取这个任务（词频-1，处理++，冷却时间+n）；否则（所有任务词频都为-1），空闲+1.返回处理+空闲时间
    public int leastInterval(char[] tasks, int n) {
        int[] freq=new int[26];
        int maxFreq=0,maxFreqCount=0;
        for(int i=0;i<tasks.length;i++){
            freq[tasks[i]-'A']++;
        }
        for(int i=0;i<26;i++){
            if(freq[i]>maxFreq){
                maxFreq=freq[i];
                maxFreqCount=1;
            }else if(freq[i]==maxFreq){
                maxFreqCount++;
            }
        }
        return Math.max(tasks.length,(maxFreq-1)*(n+1)+maxFreqCount);
    }