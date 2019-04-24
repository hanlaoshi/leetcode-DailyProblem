//主要思路是记录下翻转的链表的头和尾，分别赋值。
//方法来源：https://blog.csdn.net/a2331046/article/details/51326259


ListNode* reverseBetween(ListNode* head, int m, int n) {
    ListNode* pre = NULL;
    ListNode* cur = head;
    ListNode* tmpTail;
    for (int i = 1 ; i < m;i++){
        pre = cur;
        cur = cur->next;
    }
    tmpTail = cur;
    for (int i = m ; i <= n ; i++){
        ListNode* next = cur->next;
        cur->next = pre;
        pre = cur;
        cur = next;
    }
    if (m==1) head = pre;
    else tmpTail->next->next = pre;
    
    tmpTail->next = cur;
    return head;
}
