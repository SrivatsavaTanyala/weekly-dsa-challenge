nums = list(map(int, input("Enter the array: ").split()))

positive = 0
negative = 1

result = [0] * len(nums)

for num in nums:
    if num > 0:
        result[positive] = num
        positive += 2
    else:
        result[negative] = num
        negative += 2

print("Result:", result)

# Time Complexity: O(N)
# Space Complexity: O(N) auxiliary space