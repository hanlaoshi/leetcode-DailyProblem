//方法1（java版本）   执行用时： 35 ms  战胜83%
class Solution {
    public int myAtoi(String str) {
        if (str == null || str.length() == 0) {
//            throw new NumberFormatException("Invalid input string: " + str);
            return 0;
        }

        // 如果字符串以空格开始
        int start = 0; //从开始找第一个不是空格的数
        boolean positive = true; // 是否为正数默认为true

        if (str.charAt(start) == ' ') {
            while (str.charAt(start) == ' ') {
                start++;
                if (start >= str.length()) { // 输入的全是空格
//                    throw new NumberFormatException("Invalid input string: " + str);
                    return 0;
                }
            }
        }

        if (str.charAt(start) == '-') { // 第一个非空白字符中-
            positive = false;
            start++;
        } else if (str.charAt(start) == '+') {// 第一个非空白字符是+
            start++;
        } else if (str.charAt(start) >= '0' && str.charAt(start) <= '9') { // 第一个非空白字符是数字
            return cal(str, start, true);
        } else { // 其它情况就抛出异常
//            throw new NumberFormatException("Invalid input string: " + str);
            return 0;
        }


        if (start >= str.length()) { // 第一个非空白字符是+或者-但也是最后一个字符
//            throw new NumberFormatException("Invalid input string: " + str);
            return 0;
        }

        if (str.charAt(start) > '9' || str.charAt(start) < '0') { // +或者-后面接的不是数字
//            throw new NumberFormatException("Invalid input string: " + str);
            return 0;
        } else {
            return cal(str, start, positive);
        }
    }

    private int cal(String str, int start, boolean positive) {

        long result = 0;
        while (start < str.length() && str.charAt(start) >= '0' && str.charAt(start) <= '9') {
            result = result * 10 + (str.charAt(start) - '0');

            if (positive) { // 如果是正数
                if (result > Integer.MAX_VALUE) {
//                    throw new NumberFormatException("Invalid input string: " + str);
                    return Integer.MAX_VALUE;
                }

            } else {
                if (-result < Integer.MIN_VALUE) {
//                    throw new NumberFormatException("Invalid input string: " + str);
                    return Integer.MIN_VALUE;
                }
            }

            start++;
        }

        if (positive) {
            return (int) result;
        } else {
            return (int) -result;
        }
    }
}
