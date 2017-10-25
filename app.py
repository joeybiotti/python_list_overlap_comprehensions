import random

list_a = random.sample(range(1, 30), 15)
list_b = random.sample(range(1, 30), 20)

result = [num for num in list_a if num in list_b]

print(result)