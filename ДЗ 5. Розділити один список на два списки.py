input_list1 = [1, 2, 3, 4, 5, 6]
first_sublist1 = input_list1[:3]
second_sublist1 = input_list1[3:]
result_list1 = [first_sublist1, second_sublist1]
print(result_list1)

input_list2 = [1, 2, 3]
first_sublist2 = input_list2[:2]
second_sublist2 = [input_list2[2]]
result_list2 = [first_sublist2, second_sublist2]
print(result_list2)

input_list3 = [1, 2, 3, 4, 5]
first_sublist3 = input_list3[:3]
second_sublist3 = input_list3[3:]
result_list3 = [first_sublist3, second_sublist3]
print(result_list3)

input_list3 = [1]
first_sublist3 = input_list3[:]
second_sublist3 = input_list3[1:]
result_list3 = [first_sublist3, second_sublist3]
print(result_list3)

input_list3 = []
first_sublist3 = input_list3[:]
second_sublist3 = input_list3[:]
result_list3 = [first_sublist3, second_sublist3]
print(result_list3)


input_list = [1, 2, 3, 4, 5, 6]
if len(input_list) == 0:
    print([[], []])
elif len(input_list) % 2 == 0:
    half_length = len(input_list) // 2
    first_half = input_list[:half_length]
    second_half = input_list[half_length:]
    print([first_half, second_half])
else:  # Непарна кількість елементів
    half_length = len(input_list) // 2
    first_half = input_list[:half_length + 1]
    second_half = input_list[half_length + 1:]
    print([first_half, second_half])