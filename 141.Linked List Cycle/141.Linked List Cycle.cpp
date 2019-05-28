class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* first=head;
        ListNode* second=head;
        while(first!=NULL&&second!=NULL&&second->next!=NULL){ //注意这个条件判断不能写漏了。
            first=first->next;
            second=second->next->next;
            if(first==second)
                return true;
        }
        return false;
    }
};
