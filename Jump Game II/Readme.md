Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

`Example:`

`Input:` [2,3,1,1,4]
`Output:` 2
`Explanation: `The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
`Note:`

You can assume that you can always reach the last index.

`原题`

数组中的每个值表示在当前位置最多能向前面跳几步，判断至少跳几步能够跳到最后。

`注意点：`

所有的数字都是正数
跳的步数可以比当前的值小
保证所有的测试用例都能够跳到最后

`例子：`

`输入: `nums = [2, 3, 1, 1, 4]
`输出: `2
