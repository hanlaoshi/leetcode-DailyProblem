public NumArray(int[] nums) {
　　　　  //nums[0]不变 num[i]=num[i]+前一位
        for(int i = 1; i < nums.length; i++){
            nums[i] =nums[i]+nums[i - 1];
        }

        this.nums = nums;
    }

    public int sumRange(int i, int j) {
        if(i == 0){
            return nums[j];
        }

        return nums[j] - nums[i - 1];
    }