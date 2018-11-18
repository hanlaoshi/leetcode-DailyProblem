/*
这道题就用循环递归解决子问题。

因为求所有组合，这就意味着不能重复使用元素，要用visited数组。

有因为是所有可能的组合，所以循环length次，就是这里面每位都有可能有length个可能性。

正因为如此，每一层递归就不需要传递一个start点，告诉他从哪开始（因为都是从头开始循环）。
*/

public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> item = new ArrayList<Integer>();
        
        if(num.length==0||num==null)
            return res;
        boolean[] visited = new boolean[num.length];  
        
        permutation_helper(num,res,item,visited);
        return res;
    }
    
    public void permutation_helper(int[] num, ArrayList<ArrayList<Integer>> res, ArrayList<Integer> item,boolean[] visited){
        if(item.size()==num.length){
            res.add(new ArrayList<Integer>(item));
            return;
        }
        
        for(int i = 0; i<num.length;i++){
            if(!visited[i]){
                item.add(num[i]);
                visited[i]=true;
                permutation_helper(num,res,item,visited);
                item.remove(item.size()-1);
                visited[i]=false;
            }
        }
    }
