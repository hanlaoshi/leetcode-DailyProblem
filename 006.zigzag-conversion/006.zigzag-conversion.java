//方法1（java版本）  执行用时：31 ms  战胜百分之99的java示例

class Solution {
    public String convert(String s, int numRows) {
      //判断不为1
   if (numRows == 1 || s.length() == 1 || numRows > s.length()) return s;
      
         char[] cs = s.toCharArray();
         //获取长
         char[] res = new char[cs.length];
         //获取他的位数 4位一个长    
         int cycle = (numRows - 1) <<1;
         //替代值 用代词 循环给俩循环赋值
         int index = 0;
          //开始循环
         for(int i = 0; i < numRows; i++){
          //让i等于j
             int j = i;
             while(j < cs.length){
                 if(i == 0 || i == numRows - 1){
                  //循环为0和为最后的时候 把j带入测试
                     res[index++] = cs[j];
                     //循环j 加上总个数
                     j += cycle;
                 } else {
                  //循环中间层 把j带入测试
                     res[index++] = cs[j];
                     //循环得到k     分几层 然后减去i值再减去1进行成2 还要加上j
                     int k = j + ((numRows - i - 1) << 1);
                     //判断是否小于总数
                     if(k < cs.length)
                         res[index++] = cs[k];
                     //然后循环J 加上总数
                     j += cycle;
                 }
             }
         }
         return String.valueOf(res);
     
    }
}
