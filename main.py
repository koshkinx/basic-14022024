while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter action: ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            continue
        else:
            result = num1 / num2
    else:
        print("Invalid operator!")
        continue

    print("Your result is:", result)

    choice = input("Do you want to perform another calculation? (yes/no): ").lower()

    if choice == 'no':
        print("Exiting calculator.")
        break
    elif choice == 'yes':
        continue
    else:
        print('Please write "no" or "yes"')
        while True:
            choice = input("Do you want to perform another calculation? (yes/no): ").lower()
            if choice == 'no':
                break
            elif choice == 'yes':
                # Продолжаем выполнение цикла для ввода новых чисел и операции
                continue

    if choice == 'no':
        print("Exiting calculator.")
        break
