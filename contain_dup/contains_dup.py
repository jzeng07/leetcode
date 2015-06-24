def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


def containsNearbyDuplicate(nums, k):
    i = 0
    while i < len(nums):
        tmpnums = nums[i:k]
        tmpnums.sort()
        for j in range(len(tmpnums)-1):
            if tmpnums[i] == tmpnums[i+1]:
                return True
        i += k
    return False



print "contains duplicate"
print containsDuplicate([])    
print containsDuplicate([1])    
print containsDuplicate([1, 2, 3])    
print containsDuplicate([2, 3, 1])    
print containsDuplicate([2, 3, 2])    
print containsDuplicate([-1, 3, 2, -1])    



print "contains near by duplicate"
print containsNearbyDuplicate([], 1)    
print containsNearbyDuplicate([1], 1)    
print containsNearbyDuplicate([1, 2, 3], 2)    
print containsNearbyDuplicate([2, 3, 1], 2)    
print containsNearbyDuplicate([2, 3, 2], 3)    
print containsNearbyDuplicate([-1, 3, 2, -1], 2)    
print containsNearbyDuplicate([-1, 3, 2, -1], 4)

nums = [x for x in xrange(30000)]
print containsNearbyDuplicate(nums, len(nums))
