import dash_mantine_components as dmc

component = dmc.CodeHighlight(
    language="python",
    code="""# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, summ = nums[0], nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            summ = max(summ, curr)
        return summ""",
)
