class Solution(object):
    def pre(self, s):
        a = [0,0,0]
        b = [0 for i in range(20)]
        if len(s) == 0:
            return 3,b
        pre = s[0]
        ind = 0
        for i in range(0,len(s)):
            if ind < 20:
                if s[i] == pre:
                    b[ind] += 1
                else:
                    pre = s[i]
                    ind += 1
                    if ind < 20:
                        b[ind] += 1
            if s[i]>='a' and s[i] <='z':
                a[0] = 1
            elif s[i]>='A' and s[i] <='Z':
                a[1] = 1
            elif s[i]>='0' and s[i] <='9':
                a[2] = 1
        types = 3-sum(a)
        return types,b
    def handleLong(self, s):
        n = len(s)
        types,b = self.pre(s)
        c = [min(i,2) for i in b]
        l1 = 20-sum(c)
        if l1<=0:
            return n-20 + types
        c = [(i-2)/3*3+2 if i>2 else i for i in b]
        l2 = 20-sum(c)
        if l2 <= 0:
            return n-20 + max(types, (l1-1)/3+1)
        c = [max((i-2)/3*3+2,(i-1)/3*3+1) if i>2 else i for i in b]
        l3 = 20-sum(c)
        if l3 <= 0:
            return n-20 + max(types, (l1-l2)/3+(l2-1)/2+1)
        else:
            return n-20 + max(types, (l1-l2)/3+(l2-l3)/2+l3)
    def handeNormal(self, s):
        n = len(s)
        types,b = self.pre(s)
        r = sum([max(0,i/3) for i in b])
        return max(r,types)
    def handleSmall(self, s):
        n = len(s)
        types,b = self.pre(s)
        return max(types,6-n)

    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n > 20:
            return self.handleLong(s)
        elif n < 6:
            return self.handleSmall(s)
        else:
            return self.handeNormal(s)

t="abcd01234567890123456789A"
ans = 5
print Solution().strongPasswordChecker(t),ans
t="aaaaaaaaaabbbbbbbbbbcccccccccc"
t="aaaabbbbccccddddffffgggg"
t="aaabbbcccdddfffgggeeefff"
ans = 8
print Solution().strongPasswordChecker(t),ans
t="aaabbbAB1"
ans = 6
print Solution().strongPasswordChecker(t),ans
t=""
ans = 6
print Solution().strongPasswordChecker(t),ans
