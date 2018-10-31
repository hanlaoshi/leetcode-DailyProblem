//方法1（Java版）：暴力法  
//在这种情况下，我们将简单地考虑每对可能出现的线段组合并找出这些情况之下的最大面积。

public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i + 1; j < height.length; j++)
                maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
        return maxarea;
    }
}



