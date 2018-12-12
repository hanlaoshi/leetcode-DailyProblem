/*
题意大致如下：set S的长度为n，无序存储了数字1-n，但由于data error，有一个数字出现了重复（同时意味着有一个数字缺失），找出重复数字和缺失的数字。 
用一个map，第一遍循环，把set S过一遍，出现的数字用map标记，同时记录下重复的数字（已标记过的数字第二次读到为重复数字）。 
第二遍循环，把map过一遍，查找缺失数字（没有被标记的数字）。 
时间复杂度为o(n)。

*/

public class Solution {
    public int[] findErrorNums(int[] nums) {
        int res[]=new int[2];
        //boolean类型默认初始化为false
        boolean map[]=new boolean[nums.length+1];
        for(int i=0;i<nums.length;i++)
            if(map[nums[i]]==false)
                map[nums[i]]=true;
            else
                res[0]=nums[i];
        for(int i=1;i<(nums.length+1);i++)
            if(map[i]==false){
                res[1]=i;
                break;
            }
        return res;
    }
}
