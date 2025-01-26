def number(num):
    return [f"{i + 1}: {numbers}" for i, numbers in enumerate(num)]

print(number([1, 2, 3, 4, 5]))  # ['1: 1', '2: 2', '3: 3', '4: 4', '5: 5']
    