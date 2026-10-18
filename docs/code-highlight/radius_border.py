import dash_mantine_components as dmc

component = dmc.CodeHighlight(
    radius="xl",
    withBorder=True,
    withExpandButton=True,
    expandCodeLabel="Show full code",
    collapseCodeLabel="Show less",
    defaultExpanded=False,
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
