total_seconds = int(input("Введіть кількість секунд: "))

days = total_seconds // 86400
hours = (total_seconds % 86400) // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

days_str = "день"
if days == 1:
    days_str = "день"
else:
    if 2 <= days <= 4:
        days_str = "дні"
    else:
        days_str = "днів"

result = f"{days} {days_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print("Результат:", result)