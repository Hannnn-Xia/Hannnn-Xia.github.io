from copy import *
from typing import *
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        #O(n)
        def calculate(i):
            copyedNum = originalNum
            x = copyedNum[i]
            return a*x**2 + b*x + c
        
        
        def findClosestMiddlePoint(num, lst):
            #binary search to find point closest to a point
            left = 0
            right = len(lst) - 1
            while left < right - 1:
                mid = (left + right)//2 #would always skew to left
                if lst[mid] < num:
                    left = mid
                elif lst[mid] > num:
                    right = mid
                else:
                    return mid
            if abs(nums[left]) <= abs(nums[right]):
                return left
            else:
                return right
                
            #ch
        originalNum = nums

        if a == 0:
            if b == 0:
                return nums
            else:
                result = [calculate(i) for i in range(len(nums))]
                return result if b > 0 else reversed(result)
                
        nums = [x + b/(2*a) for x in nums]
        mid = findClosestMiddlePoint(0, nums)
        print(mid)
        
        left = mid - 1
        right = mid + 1
        
        ans = [calculate(mid)]
        while not (left == -1 or right == len(nums)):
            if abs(nums[left]) <= abs(nums[right]):
                ans.append(calculate(left))
                left -= 1
            else:
                ans.append(calculate(right))
                right += 1
        if left != -1:
            while not left == -1:
                ans.append(calculate(left))
                left -= 1
        else:
            while not right == len(nums):
                ans.append(calculate(right))
                right += 1
        
        return ans if a > 0 else reversed(ans)
                

if __name__ == '__main__':
  s = Solution()
  print(s.sortTransformedArray([-4,-2,2,4], 1, 3, 5))