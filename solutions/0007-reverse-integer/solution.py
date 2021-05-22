class Solution:
    def reverse(self, x: int) -> int:
        
        new = ''
        new_x = 0
        interm = 1
        if x<0:
            new_x = x*-1
            interm = -1
        else:
            new_x = x
        string = str(new_x)            
        rev_string = string[len(string)::-1]
        for val in rev_string:
            new += val
        final = int(new) * interm
        if final < -2**(31) or final > 2**(31):
            return 0
        else:
            return final
