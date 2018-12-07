 class Solution {
        public int search(int[] nums, int target) {
            //实际上就是两个递增序列，依旧是二分法
            //只不过只在递增序列中二分
            if(nums.length==0){
                return -1;
            }
            int st = 0,end = nums.length-1;
            while(st <= end){
                int mid = st+(end-st)/2;
                if(nums[mid]==target){
                    return mid;
                }
                if(nums[mid]>=nums[st]){
                    if(nums[st]<=target&&target<nums[mid]){
                        end = mid-1;
                    }else{
                        st = mid+1;
                    }
                }else{
                    if(nums[mid]<target&&target<=nums[end]){
                        st = mid+1;
                    }else{

                        end = mid==0?mid:mid-1;
                    }
                }
            }
            return -1;
        }
    }
