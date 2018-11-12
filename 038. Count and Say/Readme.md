The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"


`原题`

把一个数字用几个几的形式表示出来。如2就是1个2，即12。对12进行数数得到1112，依次类推。
假设初始数字是1，求第n个数是什么。起始5个数字为1, 11, 21, 1211, 111221, ...

`注意点：`

题目中的数字都用字符串表

`例子：`

输入: n = 5 输出: 111221



`解题思路`
用一个下标来表示当前统计的字符的起始位置，一个计数器来表示该字符的数目。
不断读取直到字符不相等，添加到结果集中，更新起始位置和计数器。
下面代码中的计数器用下标相减代替。
