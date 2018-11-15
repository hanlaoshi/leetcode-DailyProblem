Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


`原题`

数组中的每个值表示在当前位置最多能向前面跳几步，判断至少跳几步能够跳到最后。

`注意点：`

所有的数字都是正数
跳的步数可以比当前的值小
保证所有的测试用例都能够跳到最后
例子：

`输入:` nums = [2, 3, 1, 1, 4]
`输出:` 2
