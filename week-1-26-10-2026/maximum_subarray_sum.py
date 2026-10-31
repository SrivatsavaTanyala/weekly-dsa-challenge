nums = list(map(int, input("Enter the array: ").split()))

curr_sum = 0
max_sum = float('-inf')

for i in range(len(nums)):
    curr_sum += nums[i]
    max_sum = max(max_sum, curr_sum)

    if curr_sum < 0:
        curr_sum = 0

print("Maximum subarray sum:", max_sum)