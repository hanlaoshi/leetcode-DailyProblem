class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_map<ListNode*, bool> visited;
        while(head != NULL)
        {
            if(visited[head] == true)
                return head;
            visited[head] = true;
            head = head->next;
        }
        return NULL;
    }
};
解法二：
使用快慢指针，
fast每次前进两步(若两步中出现NULL，则返回NULL).
slow每次前进一步(若出现NULL，则返回NULL).
当出现环路，则总有某时刻，fast会赶上slow（相遇），证明如下：
1、若fast套slow圈之前在slow后方两步，则fast2slow1之后，fast在slow后方一步，进入(2)
2、若fast套slow圈之前在slow后方一步，则fast2slow1之后，fast追上slow（相遇）
其他情况均可化归到以上两步。
假设从head到环入口entry步数为x，环路长度为y，相遇时离entry的距离为m
则fast：x+ay+m，slow：x+by+m  (a > b)
x+ay+m = 2(x+by+m)
整理得x+m = (a-2b)y
以上式子的含义是，相遇时的位置(m)再前进x步，正好是y的整倍数即整圈。
现在的问题是怎样计数x。
利用head到entry的长度为x，只要fast从head每次前进一步，slow从相遇位置每次前进一步，
再次相遇的时候即环的入口。

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;
        do
        {
            if(fast != NULL)
                fast = fast->next;
            else
                return NULL;
            if(fast != NULL)
                fast = fast->next;
            else
                return NULL;
            slow = slow->next;
        }while(fast != slow);
        fast = head;
        while(fast != slow)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return slow;
    }
};