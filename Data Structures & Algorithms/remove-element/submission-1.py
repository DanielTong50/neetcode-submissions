class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #keep track of k, which represents "correct length" of
        #elements that do not have val -> start off with 0

        #go through nums (every element), if it is not equal to val
        #then we accept it and increment k

        #return k

        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k+=1
            
        return k