class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cnt = [0]
        n = len(words)
        for w in words:
            cnt.append(cnt[-1]+len(w))
        res = []
        pre = 0
        now = 1
        while now <= n:
            while now <= n and cnt[now]-cnt[pre]+now-pre-1 <= maxWidth:
                now += 1
            if now > n:
                break
            begin = pre
            end = now - 2
            spaces = maxWidth - (cnt[end+1]-cnt[begin])
            gap = end-begin
            if gap > 0:
                avg = spaces/gap
                left = spaces%gap
                res.append((" "*(avg+1)).join(words[begin:begin+left]+[""]) + (" "*avg).join(words[begin+left:end+1]))
            else:
                res.append(words[begin]+" "*spaces)
            pre = end+1
        lastline = " ".join(words[pre:])
        res.append(lastline+ " "*(maxWidth-len(lastline)))
        return res

a = ["This", "is", "an", "example", "of", "text", "justification."]
print Solution().fullJustify(a,16)
a = ["12345","2345","4"]
a = []
print Solution().fullJustify(a,4)
