class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        result=""
        for word in words:
            result+=word[0]
        if result==s:
            return True