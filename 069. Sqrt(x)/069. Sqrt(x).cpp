class Solution127_2 {
public:
    int mySqrt(int x) {
        if (x == 0 || x == 1)
            return x;
        int i = 0;
        int j = x;
        int mid;
        while (1)
        {
            mid = (i + j) / 2;
            if (mid>x / mid)
                j = mid;
            else
            {
                if ((mid + 1) > x / (mid + 1))
                    return mid;
                i = mid;
            }
        }
    }
};
