class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.split()
        l=s[-1]
        return len(l)
        