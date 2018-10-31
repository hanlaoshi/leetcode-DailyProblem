Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:
Input: "(]"
Output: false
Example 4:
Input: "([)]"
Output: false
Example 5:
Input: "{[]}"
Output: true



判断一个只包含各种括号符号的字符串中括号的匹配情况。

`注意点：`

字符串中只会包含"(",")","[","]","{","}"这些字符
括号匹配要注意顺序，字符串"([)]"是错误的匹配

`例子：`

输入: s="(){}" 输出: True
输入: s="(){}[" 输出: False
