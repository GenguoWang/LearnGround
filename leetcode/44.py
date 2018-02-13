import collections
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        queue = collections.deque()
        queue.append((0,0))
        sn = len(s)
        pn = len(p)
        old = set()
        print sn,pn
        cnt = 0
        while len(queue) > 0:
            cnt += 1
            x,y = queue.popleft()
            if x==sn and y==pn:
                print cnt
                return True
            if y == pn:
                continue
            if p[y] == '*':
                for i in range(x,sn+1):
                    cnt+=1
                    if (i,y+1) not in old:
                        old.add((i,y+1))
                        queue.append((i,y+1))
            elif p[y] == '?':
                if x!=sn and (x+1,y+1) not in old:
                    old.add((x+1,y+1))
                    queue.append((x+1,y+1))
            else:
                if x!=sn and s[x]==p[y] and (x+1,y+1) not in old:
                    old.add((x+1,y+1))
                    queue.append((x+1,y+1))
        print cnt
        return False

print Solution().isMatch("aa","*"),True
print Solution().isMatch("aa","*a"),True
print Solution().isMatch("aa","*b"),False
print Solution().isMatch("","****"),True
print Solution().isMatch("aa",""),False
print Solution().isMatch("",""),True
a = "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab"
b= "*aabb***aa**a******aa*"
print Solution().isMatch(a,b),True
a = "aaabbaaaaaabbbaabbbbaabbbabbaaaaabbbbbbbaaabbbbaabaabbababaabaabbaaabbbbbabababbbbbbabaaaaababaabaaaaaabababbbababaababbabbaabababaababbbbaaaababbbabaabbbaaaababbaabababbbabaababbbbbbbabbbbabbaabbabab"
b="******bb*a*ba*****babbbb**bb*b*aa***a*b*aaaa***bbab*b*aa*bba**a*b**b**b**b*bab*bb*a**b*a**ab*b*aabb*a*b"
print Solution().isMatch(a,b),True
a = "bbababababbababaaababbbaaababaaababbbbabaaaaabaabbaaababbbbabbabbbaaababbabbbbbbabbabababbbbabaabaabbaaaabbaaabaaabbaabababaababbaabbbbbabbbbabbbaabbabaaaaababbbaaabbbbabaababaaaababaaaabbbaaaaaababbaaba"
b = "*ba**aa*aa*aa*bbba*baaba*ab*b*b*abb*b*bb*b*****a*bba**aa*b***b***aba**baa****b***a*b**ba*ba****a*aaa"
print Solution().isMatch(a,b),True
