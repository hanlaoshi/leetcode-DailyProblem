Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19

Output: true

Explanation: 

1^2 + 9^2 = 82

8^2 + 2^2 = 68

6^2 + 8^2 = 100

1^2 + 0^2 + 0^2 = 1

写一个程序来判断一个数字是否是“happy”的。

所谓 happy number，是被这样的过程定义的数字：初始时有一个正整数，用该整数每位数字的平方之和代替这个整数，重复该过程直至数字变为1（之后不再变化），或者陷入一个无尽的循环但该循环不包括1。那些能终止于1的数字就称为 happy number。

比如：19就是一个 happy number，因为 

1^2 + 9^2 = 82

8^2 + 2^2 = 68

6^2 + 8^2 = 100

1^2 + 0^2 + 0^2 = 1
