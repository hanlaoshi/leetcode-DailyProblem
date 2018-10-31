class Solution {
    public int reverse(int c) {
            
  int temp = 0;
  int rev=0;
  while (c != 0) {
   rev = rev * 10 + c%10;
   if(temp!=rev/10){
    return 0;
   }
   temp =rev;
   c = c/10;
  }
  return rev;
 
    }
}
