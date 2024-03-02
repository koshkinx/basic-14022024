num = int(input("Введите целое число: "))

while num > 9:
    digits_product = 1
    for digit in str(num):
        digits_product *= int(digit)
    num = digits_product

print(num)