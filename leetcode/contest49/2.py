def getInd(w):
    r = [0 for i in range(26)]
    for s in w:
        r[ord(s)-97] += 1
    return r

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = {}
        self.ind = {}
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        word = self.word
        ind = self.ind
        for w in dict:
            l = len(w)
            if l not in word:
                word[l] = []
                ind[l] = []
            word[l].append(w)
            ind[l].append(getInd(w))
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        w = self.word
        l = len(word)
        if l not in w:
            return False
        ind = getInd(word)
        ws = w[l]
        inds = self.ind[l]
        for i in range(len(ws)):
            indi = inds[i]
            s = 0
            for j in range(26):
                s += abs(ind[j]-indi[j])
            if s != 2:
                continue
            s = 0
            cur = ws[i]
            for j in range(l):
                if word[j] != cur[j]:
                    if s == 0:
                        s = 1
                    else:
                        s = 2
                        break
            if s==1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
dict = ["hello", "leetcode"]
obj = MagicDictionary()
#obj.buildDict(dict)
obj.buildDict([])
print obj.search("habao")
