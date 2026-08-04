class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # validate the array size 
        # check if the element exists in the set
            # if not: store the elements in a set
            # else return true
        # else return false

        stored = set()

        for el in nums:
            if el in stored:
                return True
            else:
                stored.add(el)
        
        return False