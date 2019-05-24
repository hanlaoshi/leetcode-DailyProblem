//使用一个list来存储请求的时间，每一次调用ping函数，先把这次时间存入list中，
//然后查找list中所有和当前时间差大于3000的项并删除。接着返回list的大小即可。
//注：因为这里经常删除，所以用LinkedList的效率会更高一些(ArrayList会挪动元素)。并且删除要用iterator迭代器来删除，否则会引发ConcurrentModificationException。

class RecentCounter {
    List<Integer>list = new LinkedList();

    public RecentCounter() {
        
    }
    
    public int ping(int t) {
        list.add(t);
        Iterator<Integer> iterator = list.iterator();
        while(iterator.hasNext())
        {
            Integer a = iterator.next();
            if(t-a > 3000)
            iterator.remove();
            else break;
        }
        return list.size();
    }
}
