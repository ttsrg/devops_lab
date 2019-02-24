class Solution:
    def findComplement(self, num: int) -> int:
        self.num = num
        b = (bin(self.num)[2:])
        lengh = len(b)
        print("binary is ", b)
        print("binary length is", lengh)
        if lengh <= 32:
            b = b.replace('1', 'x')
            b = b.replace('0', '1')
            b = b.replace('x', '0')
            d = int(b, 2)
            print("inversbin ", b)
            print("decimal is ", d)
            self.num = d
        else:
            print("number is more than 32bit")
        return self.num


num = int(input())
var = Solution()
var.findComplement(num)
