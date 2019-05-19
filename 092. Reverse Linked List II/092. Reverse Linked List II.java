 /**
     *还是通过栈的方式反转，然后拼接 
     * 使用stack
     * 方法来源：https://blog.csdn.net/crazy1235/article/details/67632059
     * Runtime : 1ms
     * 
     * beats 2.94% of java submissions
     * 
     * @param head
     * @param m
     * @param n
     * @return
     */
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null || head.next == null || m >= n) {
            return head;
        }

        ListNode dummyNode = new ListNode(0);
        dummyNode.next = head;
        head = dummyNode;

        ListNode preNode = head; // pre node

        for (int i = 1; i < m; i++) {
            preNode = preNode.next;
        }

        // ----

        ListNode tempNode = preNode.next;

        Stack<ListNode> stack = new Stack<>();
        int i = 0;
        while (m + i <= n) {
            stack.push(tempNode);
            tempNode = tempNode.next;
            i++;
        }

        ListNode postNode = tempNode; // post node

        ListNode resultNode = stack.pop();
        tempNode = resultNode;

        while (!stack.isEmpty()) {
            tempNode.next = stack.pop();
            tempNode = tempNode.next;
        }

        //
        preNode.next = resultNode;
        tempNode.next = postNode;

        return dummyNode.next;
    }


//方法二
  /**
     * 通过迭代方式反转m-n的结点
     * 
     * Runtime : 0ms
     * 
     * beats 18.23% of java submissions
     * 
     * @param head
     * @param m
     * @param n
     * @return
     */
    public ListNode reverseBetween2(ListNode head, int m, int n) {
        if (head == null || head.next == null || m >= n) {
            return head;
        }

        ListNode dummyNode = new ListNode(0);
        dummyNode.next = head;
        head = dummyNode;

        ListNode preNode = head; // pre node

        for (int i = 1; i < m; i++) {
            preNode = preNode.next;
        }

        // iteration

        ListNode nodeA = preNode.next;
        ListNode nodeB = preNode.next.next;
        ListNode nodeResult = nodeA;

        int i = 0;
        while (m + i < n) {
            nodeA.next = nodeB.next;
            nodeB.next = nodeResult;
            nodeResult = nodeB;
            nodeB = nodeA.next;
            i++;
        }

        //
        preNode.next = nodeResult;

        return dummyNode.next;
    }
