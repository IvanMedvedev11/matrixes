import random
matrix = [[random.randint(0, 1000) for j in range(50)] for i in range(50)]
main_diagonal = [matrix[i][i] for i in range(50)]
diagonal = [matrix[-i - 1][i] for i in range(50)]
horizontal = matrix[25]
vertical = [matrix[i][25] for i in range(50)]
unical_main = set()
unical = set()
not_unical_main = set()
not_unical = set()
for i in range(len(main_diagonal)):
    for j in range(i + 1, len(main_diagonal)):
        if main_diagonal[i] == main_diagonal[j]:
            not_unical_main.add(main_diagonal[i])
        else:
            unical_main.add(main_diagonal[i])
for i in range(len(diagonal)):
    for j in range(i + 1, len(diagonal)):
        if diagonal[i] == diagonal[j]:
            not_unical.add(diagonal[i])
            break
        else:
            unical.add(diagonal[i])
result = []
for i in range(50):
    result.append(horizontal[i] * vertical[i])
print(*unical_main)
print(*unical)
print(*not_unical_main)
print(*not_unical)
print(*result)
