class Solution {
public:
    int calFactorial(int n){  
        int ans = 1;  
        for(int i = 1; i <= n; i++)  
            ans *= i;            
        return ans;  
    }  
      
    string getPermutation(int n, int k) {  
        string ans;  
        int num = k;  
        string s;  
        int factorial = calFactorial(n);  
          
        for(int i = 0; i < n; i++)
            s += '1' + i;
        for(int i = n; i > 0; i--){  
            factorial /= i;  
            int index = (num-1) / factorial;   
            ans += s[index];  
            num -= index * factorial;  
            s.erase(index,1);
        }  
        return ans;  
    } 
};
