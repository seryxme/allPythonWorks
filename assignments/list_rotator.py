def list_rotator(new_list, rot_num):
    count = 0
    while count < rot_num:
        rot_list = new_list[0:1]
        new_list.pop(0)
        new_list.append(rot_list[0])
        count += 1

    return new_list


num_set = [1, 2, 3, 4, 5, 6, 7]

print(list_rotator(num_set, 3))


def rotate(new_list: list[int], rot_num: int) -> list[int]:
    rot_num = rot_num % len(new_list)
    return new_list[rot_num:] + new_list[:rot_num]


print(rotate(num_set, 2))
