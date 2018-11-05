Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol         Value

I             1

V             5

X             10

L             50

C             100

D             500

M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. 

The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 

However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 

X can be placed before L (50) and C (100) to make 40 and 90. 

C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

`Example 1:`

Input: 3

Output: "III"

`Example 2:`

Input: 4

Output: "IV"

`Example 3:`

Input: 9

Output: "IX"

`Example 4:`

Input: 58

Output: "LVIII"

Explanation: L = 50, V = 5, III = 3.

`Example 5:`

Input: 1994

Output: "MCMXCIV"

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



   `原题`
   
将一个int型的数字转化为罗马数字，范围在1-3999。下面是罗马数字的介绍及基本规则：

罗马数字采用七个罗马字母作数字、即Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。记数的方法：

相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3

小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12

小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9

`注意点：`

基本数字 Ⅰ、X 、C 中的任何一个、自身连用构成数目、或者放在大数的右边连用构成数目、都不能超过三个，放在大数的左边只能用一个

不能把基本数字 V 、L 、D中的任何一个作为小数放在大数的左边采用相减的方法构成数目，放在大数的右边采用相加的方式构成数目时只能使用一个

V 和 X 左边的小数字只能用 Ⅰ

L 和 C 左边的小数字只能用 X

D 和 M 左边的小数字只能用 C

例子：

输入: num=99 输出: XCIX
