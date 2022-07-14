def three_sum(list_of_nums: list, target: int) -> list:
    for x in range(len(list_of_nums) - 2):
        for y in range(x+1, len(list_of_nums) - 1):
            for z in range(x+2, len(list_of_nums)):
                if list_of_nums[x] + list_of_nums[y] + list_of_nums[z] == target:
                    return [x, y, z]

    return []


print(three_sum([3, 1, 4, -8, 6, 11, 5], 3))