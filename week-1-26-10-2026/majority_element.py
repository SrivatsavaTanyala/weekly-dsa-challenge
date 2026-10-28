nums = list(map(int, input("Enter the array: ").split()))
n = len(nums)

freq_dict = {}

for num in nums:
    freq_dict[num] = freq_dict.get(num, 0) + 1

for key in freq_dict.keys():
    if freq_dict[key] > n / 2:
        print("Majority element:", key)
        break

# Time Complexity: O(n + n / 2) -> O(n)
# Space Complexity: O(n / 2) -> O(n)