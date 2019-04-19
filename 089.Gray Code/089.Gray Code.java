/**
递归生成码表 
这种方法基于格雷码是反射码的事实，利用递归的如下规则来构造： 
1位格雷码有两个码字 
(n+1)位格雷码中的前2n个码字等于n位格雷码的码字，按顺序书写，加前缀0 
(n+1)位格雷码中的后2n个码字等于n位格雷码的码字，按逆序书写，加前缀1 

*/
public class Solution {

    public List<Integer> grayCode(int n) {
        List<Integer> result = new LinkedList<>();
        if (n >= 0) {
            // 格雷码的前半部分
            result.add(0);
            // 格雷码最高位的值（非0时）
            int t = 1;
            // 每一次外循环求出的是位数i+1位的格雷码表，其相当于长度为i+1位的格雷码表的前半部分
            for (int i = 0; i < n; i++) {
                // 求出的长度为i+1位格雷码表的后半部分，前半部分由长度为i位的格雷码表给出
                for (int j = result.size() - 1; j >= 0; j--) {
                    result.add(result.get(j) ^ t);
                }
                // 最高位右移
                t <<= 1;
            }
        }
        return result;
    }
}
