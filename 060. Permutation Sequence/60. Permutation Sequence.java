//相当于因式分解
    public String getPermutation(int n, int k) {
        int[] factorial = new int[n];
        
        //因式分解需要的基数
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                factorial[i] = 1;
                continue;
            }
            factorial[i] = factorial[i - 1] * (i);
        }
        //1,1,2,6,24
        //1*0+1*1+2*2+6*3+24*4=119
        //而我们实际需要的数是：1、2、3、4、5，但他们的组合序列就相当于0、1、2、3、4的组合，只是各自加1而已。
        //二者的不同还在于，0-4的k的表是范围是从0-119，而我们的k是从1-120，所以变换关系是k-1。
        
 
        StringBuilder res = new StringBuilder();
        boolean[] used = new boolean[n];
        int i = n - 1;
        while (i >= 0) {
            int digit = (k - 1) / factorial[i];//变换关系k-1
            res.append(findKth(used, digit));//先取最高位的值
            k -= digit * factorial[i--];
        }
 
        return res.toString();
    }
    //再次强调下，数组是用的地址，而我们传递的对象就是普通的参数
    public int findKth(boolean[] used, int digit) {
        int res = -1;
        while (digit >= 0) {
            if (!used[++res]) { //从小到大的去取值，同时进行标记
                digit--;
            }
        }
        used[res] = true;
        return res + 1;//从0-4，变为1-5
 
    }
