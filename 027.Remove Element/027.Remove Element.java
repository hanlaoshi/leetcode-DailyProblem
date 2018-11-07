
//----------------java--------------------
public class Solution {
    public int removeElement(int[] A, int elem) {
        //{1,1,2,1,2,3,2,3,1}
        int newIndex = 0;
        for (int oldIndex = 0; oldIndex < A.length; ++oldIndex) {
            if (A[oldIndex] != elem) {
                A[newIndex++] = A[oldIndex];
            } 
        }
        return newIndex;
    }
}
