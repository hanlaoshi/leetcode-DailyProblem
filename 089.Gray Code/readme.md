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

`格雷码与二进制数转换关系`

`二进制转格雷码`

（假设以二进制为0的值做为格雷码的0）

G：格雷码 B：二进制码 n：正在计算的位 

根据格雷码的定义可得：

G(n) = B(n+1) XOR B(n) 

即 
G(n) = B(n+1) + B(n) 

自低位至高位运算即可，无需考虑进位


`格雷码转二进制`

由于G(n) = B(n+1) + B(n) 

故而B(n) = B(n+1) - G(n) 

自高位至低位运算即可，无需考虑借位。

例： 格雷码0111，为4位数，故设二进制数自第5位至第1位分别为：0 b3 b2 b1 b0。

b3= 0-0 =0

b2=b3-1=0-1=1

b1=b2-1=1-1=0

b0=b1-1=0-1=1

因此所转换为之二进制码为0101
