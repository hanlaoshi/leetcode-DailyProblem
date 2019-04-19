The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
             
             
格雷码表示在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同。现给定二进制码的位数，要求打印出格雷码序列。
注意点：

格雷码序列有多种可能，可以先改变低位或高位
例子：

输入: n = 2
输出: [0,1,3,2]
00 - 0
01 - 1
11 - 3
10 - 2
