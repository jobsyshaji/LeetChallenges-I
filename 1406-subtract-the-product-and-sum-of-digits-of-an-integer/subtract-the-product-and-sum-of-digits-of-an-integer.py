class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        pro = 1
        sum1 = 0

        while temp>0:
            r = temp%10
            
            pro = pro*r
            sum1 = sum1 + r

            temp = temp// 10

        return pro-sum1


        