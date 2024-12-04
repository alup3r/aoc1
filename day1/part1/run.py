#!/usr/bin/env python

def sorted_arrs(filename):
    # join the two columns from the input file into a list
    arr1 = []
    arr2 = []
    with open(filename, 'r') as f_obj:
        for line in f_obj:
            first, second = map(int, line.strip().split())
            arr1.append(first)
            arr2.append(second)

    # sort both newly created lists to facilitate the number pairing
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    # now that lists have been sorted create a new list from the sorted lists
    # and create the paris from the two lists
    comb_sorted_arr = [[x, y] for x, y in zip(sorted_arr1, sorted_arr2)]
    return comb_sorted_arr


def get_total_distance(arr):
    return sum(abs(first-second) for first, second in arr)

def main():
    arr = sorted_arrs("input.txt")
    total_distance = get_total_distance(arr)
    print(f"The total distance is: {total_distance}")


if __name__ == "__main__":
    main()
