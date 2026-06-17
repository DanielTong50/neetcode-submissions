class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        //m is a pointer to the back of nums1
        //n is a pointer to the back of nums2

        //m+n-1 is the start of empty space
        //if its a non-decreasing order, we can start filling the
        //array from the back (with the highest values)
        //we create pointer h to next available space m+n-1
        //we compare m-1 and n-1, see which is bigger and then
        //fills h, then h-- and whichever one wins, we decrease that

        //end case when h (which was m+n-1) reaches -1 (we have sorted everything)
        //cause we have dealt with the 0 index.

        int h = m+n-1;
        while (n > 0){
            if (m > 0 && nums1[m-1] >= nums2[n-1]){
                nums1[h] = nums1[m-1];
                m--;
            } else{
                nums1[h] = nums2[n-1];
                n--;
            }
            h--;
        }
    }
};