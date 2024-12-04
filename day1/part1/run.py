#!/usr/bin/env python

def sorted_arrs(filename):
    # join the two columns from the input file into a list
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

    # sort both newly created lists to facilitate the number pairing
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    # now that lists have been sorted create a new list from the sorted lists
    # and create the paris from the two lists
    comb_sorted_arr = []
    for n in range(len(sorted_arr1)):
        arr = [sorted_arr1[n], sorted_arr2[n]]
        comb_sorted_arr.append(arr)

    return comb_sorted_arr


# using the new list with the pairs calculate the distance between each integer
# by subtracting each pairs a value from b value. Since this is a distance being
# calculated we need the asbolute value to avoid negative numbers. Once we have
# all the distances between the paris we can add them all together to get the
# total distance
def get_total_distance(arr):
    total_distance = 0
    for n in range(len(arr)):
        distance = abs(int(arr[n][0]) - int(arr[n][1]))
        total_distance += distance
    return total_distance

def main():
    arr = sorted_arrs("input.txt")
    total_distance = get_total_distance(arr)
    print(f"The total distance is: {total_distance}")


if __name__ == "__main__":
    main()
