nums = list(map(int, input("Enter the array: ").split()))

leaders = [nums[-1]]
recent_leader = nums[-1]

i = len(nums) - 2
while i >= 0:
    if nums[i] > recent_leader:
        leaders.append(nums[i])
        recent_leader = nums[i]
    i -= 1

leaders.reverse()

print("Leaders:", leaders)

# Time Complexity: O(N)
# Space Complexity: O(N) auxiliary space