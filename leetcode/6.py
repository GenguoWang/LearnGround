class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s
        res = ""
        k = 2*(numRows-1)
        res += s[0::k]
        for i in range(1,numRows-1):
            s1 = s[i::k]
            s2 = s[k-i::k]
            res += "".join([s1[i]+s2[i] for i in range(len(s2))])
            res += s1[len(s2):]
        res += s[k-numRows+1::k]
        return res
print Solution().convert("PAYPALISHIRING",3)
