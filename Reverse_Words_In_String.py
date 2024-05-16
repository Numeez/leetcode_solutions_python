class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        words = s.split(" ")
        print(words)
        for word in words[::-1] :
            if not (len(word)==0):
               result+=word+" "
        return(result[:len(result)-1])
        
        