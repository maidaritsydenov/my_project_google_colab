numbers = [-100, 2, 3, 5, 6, 12, 24, 2323, 23213]

result = 12


def sum_native(nums: list, res: int) -> list:
    for num1 in range(len(nums)):
        for num2 in range(num1 + 1, len(nums)):
            if sum((nums[num1], nums[num2])) == res:
                return [nums[num1], nums[num2]]

    return []
