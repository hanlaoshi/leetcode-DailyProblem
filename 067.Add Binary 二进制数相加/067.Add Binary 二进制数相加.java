//------------------------------第一种------------------------------------
public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() -1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (j >= 0) sum += b.charAt(j--) - '0';
            if (i >= 0) sum += a.charAt(i--) - '0';
            sb.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }
}　　
//------------------------------第二种------------------------------------
public class AddBinary {   
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int pointerA = a.length()-1;
        int pointerB = b.length()-1;
        int carry = 0;
        while(pointerA>=0 || pointerB>=0){
            int sum = carry;
            if(pointerA>=0){
                sum += (a.charAt(pointerA)-'0');
                pointerA--;
            }
            if(pointerB>=0){
                sum += (b.charAt(pointerB)-'0');
                pointerB--;
            }
            result.append(sum%2);
            carry = sum/2;
        }
        if(carry!=0){
            result.append('1');
        }
        return result.reverse().toString();
    }
}