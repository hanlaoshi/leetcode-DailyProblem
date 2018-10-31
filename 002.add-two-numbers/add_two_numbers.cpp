class Solution {
public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int n1 = getLength(l1), n2 = getLength(l2), diff = abs(n1 - n2);
    if (n1 < n2) swap(l1, l2);
    ListNode *dummy = new ListNode(0), *cur = dummy, *right = cur;
    while (diff > 0) {
      cur->next = new ListNode(l1->val);
      if (l1->val != 9) right = cur->next;
      cur = cur->next;
      l1 = l1->next;
      --diff;
    }
    while (l1) {
      int val = l1->val + l2->val;
      if (val > 9) {
        val %= 10;
        ++right->val;
        while (right->next) {
          right->next->val = 0;
          right = right->next;
        }
        right = cur;
      }
      cur->next = new ListNode(val);
      if (val != 9) right = cur->next;
      cur = cur->next;
      l1 = l1->next;
      l2 = l2->next;
    }
    return (dummy->val == 1) ? dummy : dummy->next;
  }
  int getLength(ListNode* head) {
    int cnt = 0;
    while (head) {
      ++cnt;
      head = head->next;
    }
    return cnt;
  }
};
