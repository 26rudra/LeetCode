#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        return sum([1 for i in str(N) if int(i)!= 0 and N % int(i) == 0])    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends