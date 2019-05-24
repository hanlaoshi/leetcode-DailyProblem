class RecentCounter {
public:
    vector<int> times;
    
    RecentCounter() {
        
    }
    
    int find_start(int x){
        int l = 0,r = times.size()-1;
        while(l < r){
            int mid = (l + r) / 2;
            if(times[mid] >= x) r = mid;
            else l = mid + 1;
        }
        return l;
    }
    
    int ping(int t) {
        times.push_back(t);
        if(t <= 3000) return times.size();
        int idx = find_start(t-3000);
        return times.size()-idx;
    }
};