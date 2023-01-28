def add_thousand_separator(nums):
    return [format(num, ',') for num in nums]

nums = eval(input())
print(add_thousand_separator(nums))

