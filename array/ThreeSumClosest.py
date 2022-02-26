class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        min_dist = None
        for i in range(nums_len):
            for j in range(i+1,nums_len):
                for k in range(j+1,nums_len):
                    temp = nums[i]+nums[j]+nums[k]-target
                    dist = temp if temp>0 else -temp
                    if min_dist is None:
                        min_dist= [dist,temp+target]
                    elif min_dist[0]>dist:
                        min_dist= [dist,temp+target]
                        if min_dist[0]==0:
                            break
                        
        return min_dist[1]



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_dist = None
        best_sum = None
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                
                    sum = nums[i]+nums[j]+nums[k]
                    
                    dist = sum-target if sum-target>0 else target-sum
                    
                    if min_dist is None:
                        min_dist = dist
                        best_sum =sum
                        
                    elif min_dist>dist:
                        min_dist = dist
                        best_sum =sum
                        
                        if dist==0:
                            break
                        
        return best_sum

class Solution:
    import math
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_dist = None
        for i in range(n-2):
            j = i+1
            k = n-1
            
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                
                dist = sum-target if sum-target>0 else target-sum
                    
                if min_dist is None or min_dist>dist:
                    min_dist = dist
                    best_sum = sum
                
                if sum>target:
                    k=k-1
                
                elif sum<target:
                    j=j+1
                
                else:
                    break
                    
        return best_sum