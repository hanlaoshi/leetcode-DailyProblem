//方法1  参考：https://www.cnblogs.com/springfor/p/3879853.html
//在添加res时候判断是否res中已经存过该item了。没存过的才存保证子集唯一性。
public static void dfs(int[] S, int start, int len, ArrayList<Integer> item,ArrayList<ArrayList<Integer>> res){
        if(item.size()==len){
            if(!res.contains(item))
                res.add(new ArrayList<Integer>(item));
            return;
        }
        for(int i=start; i<S.length;i++){
            item.add(S[i]);
            dfs(S, i+1, len, item, res);
            item.remove(item.size()-1);
        }

    }
    
    public static ArrayList<ArrayList<Integer>> subsetsWithDup(int[] S) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>> ();
        ArrayList<Integer> item = new ArrayList<Integer>();
        if(S.length==0||S==null)
            return res;
        
        Arrays.sort(S);
        for(int len = 1; len<= S.length; len++)
            dfs(S,0,len,item,res);
            
        res.add(new ArrayList<Integer>());
        
        return res;
    }
    
    //方法2  参考：http://blog.csdn.net/worldwindjp/article/details/23300545
    //在DFS过程中 当有重复元素出现就只对当前这个元素走一起，其他重复元素跳过。
     public static void dfs(int[] S, int start, int len, ArrayList<Integer> item,ArrayList<ArrayList<Integer>> res){
 2         if(item.size()==len){
 3             res.add(new ArrayList<Integer>(item));
 4             return;
 5         }
 6         for(int i=start; i<S.length;i++){
 7             item.add(S[i]);
 8             dfs(S, i+1, len, item, res);
 9             item.remove(item.size()-1);
10             while(i<S.length-1&&S[i]==S[i+1])//跳过重复元素
11                 i++;
12         }
13 
14     }
15     
16     public static ArrayList<ArrayList<Integer>> subsetsWithDup(int[] S) {
17         ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>> ();
18         ArrayList<Integer> item = new ArrayList<Integer>();
19         if(S.length==0||S==null)
20             return res;
21         
22         Arrays.sort(S);
23         for(int len = 1; len<= S.length; len++)
24             dfs(S,0,len,item,res);
25             
26         res.add(new ArrayList<Integer>());
27         
28         return res;
29     }       
