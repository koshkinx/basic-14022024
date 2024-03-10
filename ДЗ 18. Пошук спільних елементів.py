def common_elements():

    multiples_of_3 = []
    for i in range(3, 101, 3):
        multiples_of_3.append(i)
    print(multiples_of_3)

    multiples_of_5 = []
    for i in range(5, 101, 5):
        multiples_of_5.append(i)
    print(multiples_of_5)

    common_elements_set = set(multiples_of_3).intersection(set(multiples_of_5))
    return common_elements_set

result = common_elements()
print("Перетин елементів списків:", result)