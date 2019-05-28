题目要求是判断链表是否有环，leetcode上链表的题都是没有头结点的，这点大家要记住。而且若链表有环，也是最后一个节点形成的环。

大家考虑这样一个问题，链表的环相当于一个圆形操场。假设有两个人在圆形操场上无限循环的跑，那么速度快的一定能追得上速度慢的。
同理，若要判断一个链表是否有环，可设计快慢指针，当快慢指针都进入环的时候，若最终两个指针相遇，必可说明链表存在环。
下面就要考虑快慢指针的步长，从跑操场的情况来看，不管慢的有多慢，快得有多快，最终肯定能相遇。同理，链表中，也可随意指定快慢指针的步长，无非就是跑的圈数多少的问题

 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode p=head;//快指针
        ListNode q=head;//慢指针
        while(p!=null&&q!=null&&p.next!=null){//边界条件是出现空指针，就返回false；
            q=q.next;
            p=p.next.next;//空指针没有next，否则会出现NullPointerException问题
            if(p==q)return true;
        }
        return false;
    }
}

reference：
        https://blog.csdn.net/shuaishuai3409/article/details/51434182
