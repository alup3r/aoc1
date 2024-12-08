from typing import Counter
from icecream import ic

with open('input.txt', 'r') as file:
    list_a, list_b = map(sorted, zip(*(map(int, line.split()) for line in file)))

counter_b = Counter(list_b)

similarity_score = sum(a * counter_b[a] for a in list_a)
ic(f'The similarity score between the lists is: {similarity_score}')
