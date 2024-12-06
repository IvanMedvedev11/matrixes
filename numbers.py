import random
numbers = [random.randint(0, 1000) for i in range(1000)]
print(numbers)
cnt = 0
for i in range(len(numbers)):
    for j in range(2, numbers[i] // 2 + 1):
        if numbers[i] % j == 0:
            break
    else:
        cnt += 1
print(f"Кол-во простых чисел: {cnt}")
