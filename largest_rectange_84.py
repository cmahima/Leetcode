def largestRectangleArea( heights) -> int:
    stack = []
    maxArea = 0

    for i, h in enumerate(heights):
        start = i
        while stack and h < stack[-1][1]:
            item, height = stack.pop()
            maxArea = max(maxArea, height * (i - item))
            start = item
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights)-i))

    return maxArea

print(largestRectangleArea(heights = [2,1,5,6,2,3]))