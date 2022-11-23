def swap(nums,s,e):
        temp = nums[s]
        nums[s] = nums[e]
        nums[e] = temp
def reverse(nums,s,e):
        while (s<e):
            swap(nums,s,e)
            s+=1
            e-=1 
class Solution(object):
     
    def rotate(self, nums, k):
        
        n = len(nums)
        k=k%n
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
        
    
              

   
