#  You can use any of this solution

# This is optimal solution in python well it is python so you can do this 
class Solution1:
    def reverse(self, x: int) -> int:
        res = 0
        if x<0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res

# This is the solution that I used and it involves some math and logic

class Solution2:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        res=0
        while x :
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if (res>MAX//10) or (res==MAX//10 and digit>=MAX%10):
                return 0
            if (res<MIN//10) or (res==MIN//10 and digit<=MIN%10):
                return 0
            res = (res*10) +digit
        return res
        