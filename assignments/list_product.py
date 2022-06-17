def list_product(new_list):
    product = 1

    for x in new_list:
        product *= x

    return product


num_set = [1, 2, 3, 4, 5, 6, 7]
print(list_product(num_set))