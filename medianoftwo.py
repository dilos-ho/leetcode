class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sortedarr = []
        size = len(nums1) + len(nums2) + 1
        index = size/2
        i = 0
        j = 0 
        if (size%2 > 0):
            while (i + j <= int(index + 1.5)):
                if ((i < len(nums1)) and (j < len(nums2))):
                    if (nums1[i] <= nums2[j]):
                        sortedarr.append(nums1[i])
                        i += 1
                    else:
                        sortedarr.append(nums2[j])
                        j += 1
                elif ((i < len(nums1)) and (j >= len(nums2))):
                    sortedarr.append(nums1[i])
                    i += 1
                elif ((i >= len(nums1)) and (j < len(nums2))):
                    sortedarr.append(nums2[j])
                    j += 1
                else:
                    break
            val = (sortedarr[int(index-1.5)] + sortedarr[int(index-0.5)])/2
            return val
        else:
            while (i + j <= index):
                if ((i < len(nums1)) and (j < len(nums2))):
                    if (nums1[i] <= nums2[j]):
                        sortedarr.append(nums1[i])
                        i += 1
                    else:
                        sortedarr.append(nums2[j])
                        j += 1
                elif ((i < len(nums1)) and (j >= len(nums2))):
                    sortedarr.append(nums1[i])
                    i += 1
                elif ((i >= len(nums1)) and (j < len(nums2))):
                    sortedarr.append(nums2[j])
                    j += 1
                else:
                    break
            return sortedarr[int(index-1)]
            
a = Solution()
b = a.findMedianSortedArrays([1,2],[3,4])
print (b)
            
