#User function Template for python3
def intTorevbin(x):
    y = format(x, '032b')
    return y[::-1]

def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal
    
class Solution:
    def reversedBits(self, X):
        # code here 
        n=intTorevbin(X)
        n=int(n)
        m=binaryTodecimal(n)
        
        return m
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends