/**
这道题是经典的双指针问题，用两个指针一前一后指向链表。如果两个指针指向的值相等，那么就让第二个指针一直往后挪，挪到与第一个指针不同为止。然后让第一个指针的next指向第二个指针，两个指针同时往后挪，进行下面的操作。

需要注意，当list的结尾几个node是重复的时候，例如1->2->3->3，那么ptr2会指向null，需要特殊处理，令ptr1.next = null，这样list尾部就不会丢。

其他情况就不用特殊处理结尾了，因为结尾没有重复值，只须遍历就够了，不用特殊处理尾部。
*/
public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)
            return head;
        
        ListNode ptr1 = head;
        ListNode ptr2 = head.next;
        
        while(ptr2!=null){
            if(ptr1.val == ptr2.val){
                ptr2 = ptr2.next;
                if(ptr2==null)
                    ptr1.next = null;
            }else{
                ptr1.next = ptr2;
                ptr1 = ptr1.next;
                ptr2 = ptr2.next;
            }
        }

        return head;
    }
