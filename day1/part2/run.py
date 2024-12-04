#!/usr/bin/env python

from collections import Counter


def combine_arrs(filename):
    arr1 = []
    arr2 = []
    with open(filename, 'r') as f_obj:
        for line in f_obj:
            first, second = map(int, line.strip().split())
            arr1.append(first)
            arr2.append(second)
    return arr1, arr2


def calc_similarity_score(arr1, arr2):
    arr2_counter = Counter(arr2)
    similarity_score = 0
    for num in arr1:
        similarity_score += num * arr2_counter.get(num, 0)
    return similarity_score


def main():
    arr1, arr2 = combine_arrs("input.txt")
    print(calc_similarity_score(arr1, arr2))


if __name__ == "__main__":
    main()
