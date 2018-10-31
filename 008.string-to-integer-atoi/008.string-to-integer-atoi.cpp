class Solution {
public:
    int myAtoi(string str) {
        int n = str.size();
        int i;
        int flag = 0;
        long ans = 0;
        for(i = 0 ; i < n ; i ++){
           if(flag == 0){
               if(str[i] == '+') flag = 1;
               else if(str[i] == '-') flag = -1;
               else if(str[i] == ' ')   continue;
               else if(str[i] >= '0' && str[i] <= '9'){
                   ans = str[i] - '0';
                   flag = 1;
               }
               else return 0;
           }
           else{
               if(str[i] >= '0' && str[i] <= '9'){
                    ans = ans * 10 + (str[i] - '0');
                    if(ans * flag < INT_MIN) return INT_MIN;
                    if(ans * flag > INT_MAX) return INT_MAX;
               }
               else if(ans != 0)    break;
               else return 0;
           }
        }     
        return ans * flag;
    }
};
