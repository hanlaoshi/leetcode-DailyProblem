#### [933. 最近的请求次数](https://leetcode-cn.com/problems/number-of-recent-calls/)

难度简单

写一个 `RecentCounter` 类来计算最近的请求。

它只有一个方法：`ping(int t)`，其中 `t` 代表以毫秒为单位的某个时间。

返回从 3000 毫秒前到现在的 `ping` 数。

任何处于 `[t - 3000, t]` 时间范围之内的 `ping` 都将会被计算在内，包括当前（指 `t` 时刻）的 `ping`。

保证每次对 `ping` 的调用都使用比之前更大的 `t` 值。

 

**示例：**

```
输入：inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
输出：[null,1,2,3,3]
```

 

**提示：**

1. 每个测试用例最多调用 `10000` 次 `ping`。
2. 每个测试用例会使用严格递增的 `t` 值来调用 `ping`。
3. 每次调用 `ping` 都有 `1 <= t <= 10^9`。



933. Number of Recent Calls

Easy

Write a class `RecentCounter` to count recent requests.

It has only one method: `ping(int t)`, where t represents some time in milliseconds.

Return the number of `ping`s that have been made from 3000 milliseconds ago until now.

Any ping with time in `[t - 3000, t]` will count, including the current ping.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than before.

 

**Example 1:**

```
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
```

 

**Note:**

1. Each test case will have at most `10000` calls to `ping`.
2. Each test case will call `ping` with strictly increasing values of `t`.
3. Each call to ping will have `1 <= t <= 10^9`.

 