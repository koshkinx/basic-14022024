lst = []
if not lst:
    result = 0
else:
    sum_even = 0
    for i in range(0, len(lst), 2):
        sum_even += lst[i]
    result = sum_even * lst[-1]
print(result)


lst1 = [1, 3, 5]
result1 = 0
if not lst1:
    result1 = 0
else:
    sum_even1 = 0
    for i in range(len(lst1)):
        if i % 2 == 0:
            sum_even1 += lst1[i]
    result1 = sum_even1 * lst1[-1]
print(result1)