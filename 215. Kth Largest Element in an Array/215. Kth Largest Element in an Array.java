1，找第一个出现一次的字符时候，从计数数组出发，找到计数为1的。定义一个变量记录位置最小值，最后返回。（这种方向适合字符串大的）。

public static int firstUniqChar(String s) {
        int[] num = new int[26];
        boolean flag = true;
        int min = s.length();
        for(int i=0;i<s.length();i++) {
            num[s.charAt(i) - 'a']++;
        }
        for(int i = 0;i<num.length;i++) {//从计数数组出发
            int now = s.indexOf(i+'a');
            if(num[i] == 1 && now < min) {
                flag = false;
                min = now;
            }
        }
        if(flag) 
            return -1;
        return min;
    }

2，找第一个出现一次的字符时候，从字符串出发。找到第一个计数为1的就可以返回了。（适合字符串小的，leetcode的测试数据都较小，用这个更快）

public static int firstUniqChar2(String s) {
         if(null == s || 0 == s.length() ) return -1;
         int[] hash = new int[26];
         char[] array = s.toCharArray();
         for(int i = 0; i < array.length; i++){      
             int num = array[i] - 'a';
             hash[num]++;
         }
         for(int i = 0; i < array.length; i++){//从字符串出发
             int num = array[i] - 'a';
             if(hash[num] == 1){
                 return i;
             }
         }
         return -1;
    }