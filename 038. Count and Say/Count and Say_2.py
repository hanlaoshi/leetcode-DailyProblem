
def Next(s): 
  st="1
  for i in range(len(s)):
    if i!=0 and s[i]==s[i-1]:
      pass
    else: count=1
          while i+count < len(s) and s[i]==s[i+ count]:
            count+=1
    st += str(count)+s[i]
  return st
  
 s = '1'
 n = 6
 for i in range(1,n):
    s = Next(s)
 print s
  
