def max_sumDig(nMax, maxSum):
    num_list = []
    result_list = []

    def breaker(*args):
        return [int(x) for x in args]

    def rotate(lst: list[int], rot_num: int) -> list[int]:
        rot_num = rot_num % len(new_list)
        return new_list[rot_num:] + new_list[:rot_num]

    for num in range(1000, nMax + 1):
        num_of_digits = len(str(num))
        digit_list = breaker(*str(num))

        if num_of_digits == 4:
            if sum(digit_list) <= maxSum:
                num_list.append(num)
        elif num_of_digits > 4:
            digit_sum = []
            for rot in range(num_of_digits - 3):
                total = 0
                new_list = rotate(digit_list, rot)
                for x in range(4):
                    total += new_list[x]
                digit_sum.append(total)
            b = True

            for x in digit_sum:
                if x > maxSum:
                    b = False
                    break
            if b:
                num_list.append(num)

    result_list.append(len(num_list))
    mean = sum(num_list) / len(num_list)

    for x in range(len(num_list)):
        if num_list[x] == mean:
            result_list.append(num_list[x])
            break
        elif abs(mean - num_list[x]) < abs(mean - num_list[x + 1]):
            result_list.append(num_list[x])
            break

    result_list.append(sum(num_list))

    return result_list


print(max_sumDig(37021, 3))
