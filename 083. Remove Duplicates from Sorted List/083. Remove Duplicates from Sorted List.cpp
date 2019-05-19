//每个元素只保留一次，多个重复元素一次删除。

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
    	if(head == NULL || head->next == NULL)
    	{
    		return head;
    	}
 
    	ListNode *pre = head;
    	ListNode *cur = head->next;
 
    	while(cur != NULL)
    	{
    		if(cur->val != pre->val)
    		{
    			pre = cur;
    			cur = cur->next;
    			continue;
    		}
 
    		while(cur->next != NULL && cur->next->val == pre->val)
    		{
    			cur = cur->next;
    		}
 
    		pre->next = cur->next;
    		cur = pre->next;
    	}
 
    	return head;
    }
};
