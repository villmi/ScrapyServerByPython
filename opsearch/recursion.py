class Solution:
    def match(self, str1, pattern):
        if str1 is None or pattern is None:
            return False
        return self.matchCore(str1, 0, pattern, 0)

    def matchCore(self, str1, sindex, pattern, pindex):
        if(sindex == len(str1)) and (pindex == len(pattern)):
            return True
        if(pindex == len(pattern)) and (sindex != len(str1)):
            return False
        if(sindex == len(str1)) and (pindex != len(pindex)):
            if(pindex+1 < len(pattern)) and (pattern[pindex + 1] == '*'):
                return self.matchCore(str1, sindex, pattern, pindex + 2)
            else:
                return False
        if(pindex + 1 < len(pattern)) and (pattern[pindex + 1] == '*'):
            if (pattern[pindex] == str1[sindex]) or pattern[pindex] == '.':
                return (self.matchCore(str1, sindex + 1, pattern, pindex + 2) or
                        self.matchCore(str1, sindex + 1, pattern, pindex) or
                        self.matchCore(str1, sindex, pattern, pindex + 2))
            if pattern[pindex] != str1[sindex]:
                return self.matchCore(str1, sindex, pattern, pindex + 2)
        elif(pattern[pindex] == str1[sindex]) or pattern[pindex] == '.':
            return self.matchCore(str1, sindex + 1, pattern, pindex + 1)
        return False
