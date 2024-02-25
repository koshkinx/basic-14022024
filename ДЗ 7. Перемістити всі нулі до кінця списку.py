lst = [0, 1, 0, 12, 3]
for _ in range(lst.count(0)):
    lst.append(lst.pop(lst.index(0)))
print(lst)



lst_1 = [0]
zeros = [x for x in lst_1 if x == 0]
result = [x for x in lst_1 if x != 0]
result.extend(zeros)
print(result)