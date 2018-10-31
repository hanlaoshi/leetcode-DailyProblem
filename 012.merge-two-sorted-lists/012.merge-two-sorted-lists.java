public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode helper = new ListNode(0);
    ListNode pre = helper;
    helper.next = l1;
    while(l1!=null && l2 != null)
    {
        if(l1.val>l2.val)
        {
            ListNode next = l2.next;
            l2.next = pre.next;
            pre.next = l2;
            l2 = next;
        }
        else
        {
            l1 = l1.next;
        }
        pre = pre.next;
 
    }
    if(l2!=null)
    {
        pre.next = l2;
    }
    return helper.next;
}
