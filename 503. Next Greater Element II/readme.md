Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]

Output: [2,-1,2]

Explanation: The first 1's next greater number is 2; 

The number 2 can't find next greater number; 

The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.


给定一个圆形数组（最后一个元素的下一个元素是数组的第一个元素），为每个元素打印Next Greater Number。下一个更大的数字x是数组中下一个遍历顺序的第一个更大的数字，这意味着您可以循环搜索以查找其下一个更大的数字。如果它不存在，则为此数字输出-1。

例1：

输入： [1,2,1]

 输出： [2，-1,2]
 
 说明：第一个1的下一个更大的数字是2; 
 
数字2找不到下一个更大的数字; 

第二个1的下一个更大的数字需要循环搜索，这也是2。

注意： 给定数组的长度不超过10000。
