#TC - O(logn)
#SC - O(1)
class Solution(object):
    def search(ar, size):
    # Extreme cases
        if(ar[0] != 1):
            return 1
        if(ar[size-1] != (size+1)):
            return size+1

        l = 0
        h = size - 1
        mid = 0
        while h > l+1 :
            mid = (l + h) // 2
            if (ar[l] - l) != (ar[mid] - mid):
                h = mid 
            elif (ar[h] - h) != (ar[mid] - mid):
                l = mid
        return ar[l] + 1
obj = Solution
a = [1, 2, 3, 4, 5, 6, 8]
n = len(a)

print("Missing number:", obj.search(a, n))