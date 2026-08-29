class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = 1
        #goes through whole nums and multiplies
        zero_index = None
        zero_index_bool = False
        more_than_one_bool = False
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
                if zero_index_bool:
                    more_than_one_bool = True
                    #then we know everything will be 0
                else:
                    zero_index_bool = True
                    #then we have 1 zero
            else: #otherwise we multipliy normally
                result*=nums[i]

        #case where there are more than 1 zero -> return all 0
        if more_than_one_bool:
           return [0] * len(nums)
        #case where there are only 1 zero -> return all zero except that one
        elif zero_index_bool and len(nums) ==1:
            return [0]
        elif zero_index_bool:
            result_array = [0] *len(nums)
            result_array[zero_index] = result
            return result_array   
        else:
            result_array = [result]*len(nums)
            for i in range(len(nums)):
                result_array[i] = int(result_array[i]/nums[i])
            return result_array
        
            