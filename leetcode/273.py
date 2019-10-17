class Solution(object):
    def underThousand(self, num):
        N = [
            ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"],
            ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        ]
        a = num%100
        res = ""
        if a < 20:
            res = N[0][a] + " " + res
            num /= 100
        else:
            for i in range(2):
                a = num%10
                res = N[i][a] + " " + res
                num /= 10
        if num > 0:
            res = N[0][num] + " Hundred " + res
        return res.strip()
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        N = ["","Thousand","Million","Billion"]
        res = ""
        for i in range(4):
            a = num%1000
            if a > 0:
                res = self.underThousand(a)+" "+N[i]+" "+res
            num /= 1000
        return res.strip()

print Solution().numberToWords(123)
print Solution().numberToWords(12345)
print Solution().numberToWords(1234567)
print Solution().numberToWords(0)
print Solution().numberToWords(3)
print Solution().numberToWords(13)
print Solution().numberToWords(20)
print Solution().numberToWords(13000)
print Solution().numberToWords(13003)
        
