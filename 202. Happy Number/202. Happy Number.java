/*
按照题目的描述，需要循环求平方和，即求出当前数组的平方和后，再以此平方和作为新的数继续求平方和，而循环终止条件是：
得到的平方和为1，或得到的平方和在之前的循环中出现过。判断平方和是否为1很简单，每次检查就好了；而判断平方和是否出现过，
则只需要维持一个Set，每次循环检查当前平方和是否在Set中，在则终止循环，不在则将此平方和放到Set中。

*/

public class Solution {
    public boolean isHappy(int n) {
        Set<Integer> got = new HashSet<>();
        while (n != 1 && !got.contains(n)) {
            got.add(n);
            int sum = 0;
            while (n != 0) {
                sum += Math.pow(n % 10, 2);
                n /= 10;
            }
            n = sum;
        }
        return n == 1;
    }
}


//方法二   by 初夏大佬

class Solution {
    public int reverse(int x) {
        if((x<=0 && x>-10)||(x<10&&x>0)){
            return x;
        }
        
        long result = 0;
        while(x != 0 ){
            result = result*10 + x%10;
            x = x/10;
        }
        
        if(result <= Integer.MIN_VALUE || result >= Integer.MAX_VALUE){
            return 0;
        }
        
        return (int)result;
    }
}
