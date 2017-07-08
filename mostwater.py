class Solution(object):
    def maxArea(self, height):
        #work from both sides inwards
        maxWater = 0;
        start = 0;
        end = len(height) - 1;
        while (start < end):
            maxWater = max(maxWater, min(height[start],height[end])*(end-start));
            if (height[start] < height[end]):
                start += 1;
            else:
                end -= 1;
        return maxWater;
        
a = Solution();
print(a.maxArea([1,2,1]));
