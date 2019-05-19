1、两个栈，从前向后和从后向前，然后判断两个栈是否相同。

public class Solution {
    public boolean isPalindrome(String s) {
        Stack stack1 = new Stack<Character>();
        Stack stack2 = new Stack<Character>();
        s = s.toLowerCase();
        char[] word = s.toCharArray();
        int len = s.length();
        for( int i = 0;i<len;i++){
            if( (word[i] >= '0' && word[i] <= '9') || (word[i]>='a' && word[i]<='z')  )
                stack1.push(word[i]);
            if( (word[len-1-i] >= '0' && word[len-1-i] <= '9') || (word[len-1-i]>='a' && word[len-1-i]<='z')  )
                stack2.push(word[len-1-i]);
        }


        return stack1.equals(stack2);
        
    }
}

2、直接用两个指针记录left和right即可。

public class Solution {
    public boolean isPalindrome(String s) {
        
        char[] word = s.toLowerCase().toCharArray();
        int len = s.length();
        int left = 0,right = len-1;
        while( left < right ){

            if( !((word[left] >= '0' && word[left] <= '9') || (word[left]>='a' && word[left]<='z' )) )
                left++;
            else if( !((word[right] >= '0' && word[right] <= '9') || (word[right]>='a' && word[right]<='z' )) )
                right--;
            else if( word[left] == word[right]){
                left++;
                right--;
            }else
                return false;
        }
        return true;

        
        
    }
}