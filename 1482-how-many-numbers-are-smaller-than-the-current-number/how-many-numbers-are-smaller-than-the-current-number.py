class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        xdic = {}

        for i, numero in enumerate(temp):
            if numero not in xdic:
                xdic[numero] = i 
        answ = []
        for i in nums:
            answ.append(xdic[i])
        
        return answ;
        