class place{
public:
    int idx;
    int height;
    
    place(int idx, int height){
        this->idx = idx;
        this->height = height;
    }
};


int trap(vector<int>& height) {
    
    if(height.size() == 0){
        return 0;
    }

    // 计算从左往右的递增区间

    queue<place*> qL;
    
    place* tmpp = new place(0, height[0]);
    
    qL.push(tmpp);
    
    
    for (int i = 1; i < height.size(); i++) {
        
        if (height[i] >= qL.back()->height) {
            place* tmpp = new place(i, height[i]);
            qL.push(tmpp);
        }
    }    
    
    int totalRectL = 0;
    
    while (qL.size() > 1 ) {
        place* tmpp = qL.front();
        qL.pop();
        
        int len = qL.front()->idx - tmpp->idx;
                
        totalRectL += (tmpp->height * len);
        
    }
    
    place* heighestL = qL.front();
    qL.pop();
    
    int earthAmtL = 0 ;
    for (int i = 0 ; i < heighestL->idx; i++) {
        earthAmtL += height[i];
    }
    
    int waterL = totalRectL - earthAmtL;
    

    // 计算剩余的从右往左的递增区间
    queue<place*> qR;
    
    tmpp = new place((int)height.size()-1,height[height.size()-1]);
    
    qR.push(tmpp);
    for (int i = (int)height.size()-2; i >= heighestL->idx; i--) {
        if (height[i] >= qR.back()->height) {
            tmpp = new place(i, height[i]);
            qR.push(tmpp);
        }
    }
    
    int rectR = 0;
    while (qR.size() > 1) {
        place* tmpp = qR.front();
        qR.pop();
        
        int len = tmpp->idx - qR.front()->idx;
                
        rectR += tmpp->height * len;
    }
    
    place* heighestR = qR.front();
    qR.pop();
    
    int earthAmtR = 0;
    for (int i = (int)height.size()-1; heighestR->idx < i ; i--) {
        earthAmtR += height[i];
    }
    
    int waterR = rectR - earthAmtR;    

    int res = waterL + waterR;
    
    return res;
}