class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 2**31 -1 or x<0:
            return False
        
        temp = str(x)
        digits = len(temp)
    

        fro = 0
        back = digits -1

        while True:
            
            if temp[fro] == temp[back]:

                fro += 1
                back -=1
            else:
                return False
                

            if fro > back:
                return True
                
            
