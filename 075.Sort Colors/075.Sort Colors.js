//---------------狐狸-------------------------
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let start = 0;
  let end = 0;
  let num1 = 0;
  let num2 = 0;
  for (let i = 0; i < nums.length; i++) {
    switch (nums[i]) {
      case 0:
        nums[start++] = 0;
        if (num1) {
          nums[end++] = 1;
        } else {
          end++;
        }
        if (num2) {
          nums[i] = 2;
        }
        break;
      case 1:
        num1++;
        nums[end++] = 1;
        if (num2) {
          nums[i] = 2;
        }
        break;
      case 2:
        num2++;
        break;
    }
  }
};