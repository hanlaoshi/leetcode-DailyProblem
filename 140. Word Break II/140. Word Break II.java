List<String> result;
    public List<String> wordBreak(String s, Set<String> wordDict) {
        result = new ArrayList<String>();
        int n = s.length();
        //对每一个i都形成一个可以跳跃的点
        List<Integer>[] pointer = new List[n];
        for(int i=0;i<n;i++) pointer[i]=new ArrayList<Integer>();
        //动态规划形成跳跃点
        for(int i=0;i<n;i++){
            for(int j=0;j<=i;j++){
                //递归的保证j-1可以形成单词，大大地剪枝
                if(wordDict.contains(s.substring(j,i+1))&&(j==0||pointer[j-1].size()>0))
                    pointer[i].add(j);
            }
        }
        //从后往前的递归
        helper(pointer, s, n-1, "");
        return result;
    }
    //DFS
    public void helper(List<Integer>[] pointer, String s, int i, String pattern){
        if(i<0){
            result.add(pattern);
            return;
        }
        for(Integer item:pointer[i]){
            String nextPattern = pattern.length()==0?s.substring(item,i+1):s.substring(item,i+1)+" "+pattern;
            helper(pointer, s, item-1, nextPattern);
        }
    }
