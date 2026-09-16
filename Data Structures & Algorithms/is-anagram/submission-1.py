class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        adict = {}
        bdict = {}
        for l in s:
            adict[l] = adict.get(l,0) + 1
        for l in t:
            bdict[l]=bdict.get(l,0) + 1
        return adict==bdict