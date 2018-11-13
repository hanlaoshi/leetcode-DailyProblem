Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


`原题`

在一个集合（没有重复数字）中找到和为特定值的所有组合。

`注意点：`

所有数字都是正数
组合中的数字要按照从小到大的顺序
原集合中的数字可以出现重复多次
结果集中不能够有重复的组合
虽然是集合，但传入的参数类型是列表

`例子：`

输入: candidates = [2, 3, 6, 7], target = 7
输出: [[2, 2, 3], [7]]
