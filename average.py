def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Пример использования
numbers = [2, 4, 6, 8, 10, 12]
result = calculate_average(numbers)
print(f"Среднее значение: {result}")