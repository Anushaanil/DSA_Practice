def rearrangeArray(nums: list[int]) -> list[int]:
        ans = []
        while nums:
            ans.extend(sorted(set(nums)))
            [nums.remove(num) for num in nums if num in set(nums)]

        return ans

# nums = [3,1,3,2,1,3]
# ans = rearrangeArray(nums)
# print(ans)
