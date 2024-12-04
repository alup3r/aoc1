#!/usr/bin/env python

def combine_arrs(filename):
    with open(filename, 'r') as f_obj:
        content = f_obj.read()
        content_list = content.split()
    arr1 = []
    arr2 = []
    # iterate through the entire content list and pslit it into two distinct
    # lists that contain the two columns from the original input file
    for n in range(len(content_list)):
        if n % 2 == 0:
            arr1.append(content_list[n])
        else:
            arr2.append(content_list[n])
    return arr1, arr2


def calc_similarity_score(arr1, arr2):
    similarity_score = 0
    for n in range(len(arr1)):
        counter = 0
        for j in range(len(arr2)):
            if arr1[n] == arr2[j]:
                counter += 1
        similarity_score += int(arr1[n]) * counter
    return similarity_score


def main():
    arr1, arr2 = combine_arrs("input.txt")
    print(calc_similarity_score(arr1, arr2))


if __name__ == "__main__":
    main()
