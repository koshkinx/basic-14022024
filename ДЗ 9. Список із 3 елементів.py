import random

list_length = random.randint(3, 10)

random_list = []
for _ in range(list_length):
    random_list.append(random.randint(0, 99))
print(random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]
print(new_list)
