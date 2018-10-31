Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false



给定输入字符串（s）和模式（p），实现与支持'.'和的正则表达式匹配'*'。

'' 匹配任何单个字符。
'*'匹配前面元素的零个或多个。
匹配应覆盖整个输入字符串（非部分）。

注意：

s 可能是空的，只包含小写字母a-z。
p可能是空的，只包含小写字母a-z和字符，如  . 或  *。
例1：

输入：
s =“aa”
p =“a”
输出： false
 说明： “a”与整个字符串“aa”不匹配。
例2：

输入：
s =“aa”
p =“a *”
输出： true
 说明：  '*'表示零个或多个前面元素'a'。因此，通过重复“a”一次，它变为“aa”。
例3：

输入：
s =“ab”
p =“。*”
输出： true
 说明：  “。*”表示“零或多个（*）任何字符（。）”。
例4：

输入：
s =“aab”
p =“c * a * b”
输出： true
 说明：  c可重复0次，a可重复1次。因此它匹配“aab”。
例5：

输入：
s =“密西西比”
p =“mis * is * p *。”
输出： false


`思路`

绝对称得上是一道难题了这里最难的是对*的处理，有三种情况

    a*完全不匹配，即需要跳过 *以及 *前面的字母；

    a* 只匹配一个字母

    a* 匹配多个有两种方法：


`动态规划`

    因为具有递归性质、重叠子问题的性质，所以可以用动态规划来考虑。

dp[i][j]表示s前i个和p前j个匹配，注意这里假设字符串前面都有一个空串，dp[1][1]表示s的第一个字母和p的第一个字母匹配，而不是前两个！！

然后就可以考虑下面几种情况：
