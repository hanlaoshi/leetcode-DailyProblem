class Solution {
         public boolean isMatch(String s, String p) {
            if(s == null || p==null){
                return false;
            }
            return match(s,0,p,0);
        }
        private boolean match(String s,int s1,String p,int p1){
            boolean isStrDone = s1>=s.length();
            boolean isPatDone = p1>=p.length();

            if(isStrDone&&isPatDone){
                return true;
            }
            if(!isStrDone&&isPatDone){
                return false;
            }
            //一、下一个字符是*
            if(p1+1<p.length()&&p.charAt(p1+1)=='*'){
                if(isStrDone){
                    return match(s,s1,p,p1+2);
                }
                if(p.charAt(p1)==s.charAt(s1)||p.charAt(p1)=='.'&&s.charAt(s1)!='\0'){
                    return match(s,s1+1,p,p1)||match(s,s1,p,p1+2);
                }else{
                    return match(s,s1,p,p1+2);
                }
            }
            if(isStrDone&&!isPatDone){
                return false;
            }

            //二、下一个字符不是*
            if(p.charAt(p1)==s.charAt(s1)||p.charAt(p1)=='.'&&s.charAt(s1)!='\0'){
                return match(s,s1+1,p,p1+1);
            }
            return false;

        }
    }
