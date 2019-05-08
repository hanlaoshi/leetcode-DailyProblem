public class AddBinary {
    //倒序遍历
    public static String addBinary(String a, String b) {
        int aIndex = a.length() - 1;//字符数组的索引
        int bIndex = b.length() - 1;
        String result = "";//结果字符串，通过新的结果+原来的结果=构成
        int carryBit = 0;//进位
        while (aIndex >= 0 || bIndex >= 0) {
            //三种情况，a，b的指针都还在
            if (aIndex >= 0 && bIndex >= 0) {
                //在ascii中，字符'0'，'1'，'2' ...是升序的，所以字符减去'0'就是差值，也就是int本身
                //当然这里也可以使用Integer.valueOf方法去转换char为int
                int tmpBit = a.charAt(aIndex) - '0' + b.charAt(bIndex) - '0' + carryBit;//上次和进位值，加上当前两个串某位值
                result = String.valueOf(tmpBit % 2) + result;//获得当前位求余2的结果
                carryBit = tmpBit / 2;//更新进位值，除以2
                aIndex--;
                bIndex--;
            } else if (aIndex >= 0) {//只有a string
                int tmpBit = a.charAt(aIndex) - '0' + carryBit;
                result = String.valueOf(tmpBit % 2) + result;//获得当前位求余2的结果
                carryBit = tmpBit / 2;//更新进位值，除以2
                aIndex--;
            } else {//bLen>=0 ，只有b string
                int tmpBit = b.charAt(bIndex) - '0' + carryBit;
                result = String.valueOf(tmpBit % 2) + result;//获得当前位求余2的结果
                carryBit = tmpBit / 2;//更新进位值，除以2
                bIndex--;
            }
        }
        if (carryBit == 1) {//必须考虑最后进位，如果是1需要加上
            result = "1" + result;
        }
        return result;
    }
 
    //方法的代码冗余的很多，可以精简提炼
    public static String addBinary2(String a, String b) {
        String result = "";//结果集
        int carryBit = 0;//进位
        int aIndex = a.length() - 1;//索引
        int bIndex = b.length() - 1;
        while (aIndex >= 0 || bIndex >= 0) {
            //每次遍历，都定义两个字符数组的位值，根据索引是否小于0判断，是不是使用0
            int tmpA = aIndex>=0? Integer.valueOf(""+a.charAt(aIndex)):0;
            int tmpB = bIndex>=0?Integer.valueOf(""+b.charAt(bIndex)):0;
            int tmpResult = tmpA+tmpB+carryBit;
            result = tmpResult%2+result;
            carryBit = tmpResult/2;
            aIndex--;//索引都减1
            bIndex--;
        }
        if(carryBit == 1){
            result = "1"+result;
        }
        return result;
    }
 
    public static void main(String[] args) {
        System.out.println(addBinary("11", "1"));
    }
}