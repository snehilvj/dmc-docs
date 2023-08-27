import dash_mantine_components as dmc

component = dmc.Prism(
    language="python",
    children="""# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, summ = nums[0], nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            summ = max(summ, curr)
        return summ""",
)
