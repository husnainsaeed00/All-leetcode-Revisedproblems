class Solution:
    def covert(self, s:str, numRows:int) -> str:
        if numRows==1: return s

        res= ""
        for r in range(numRows):
            increment = 2 * (numRows-1)
            for i in range(r, len(s), increment):
                res += s[i]
                # we need to check that are we in the middle rows because they have different approach
                if (r > 0 and r <numRows-1 and 
                    i + increment - 2*r < len(s)):
                    res+= s[i + increment - 2*r]