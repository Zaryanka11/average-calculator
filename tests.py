def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Тест 1: Проверка среднего значения для непустого списка чисел
numbers = [2, 4, 6, 8, 10]
expected_result = 6.0
result = calculate_average(numbers)
print(f"Тест 1: Среднее значение: {result}")
assert result == expected_result, "Ошибка: Неправильное среднее значение!"

# Тест 2: Проверка среднего значения для пустого списка чисел
numbers = []
expected_result = None
result = calculate_average(numbers)
print(f"Тест 2: Среднее значение: {result}")
assert result == expected_result, "Ошибка: Неправильное среднее значение!"
