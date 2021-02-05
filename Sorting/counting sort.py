"""Implement the counting sort."""


def countingSort(arr):
    # Task1: Count the range of the elements, then create a count and a output array
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = (max_element - min_element) + 1

    count_array = [0] * range_of_elements
    output_array = [0] * len(arr)

    # Task 2: Store the count of each element
    for i in range(0, len(arr)):
        count_array[arr[i] - min_element] += 1

    # Task 3: Change the count to actual position in the output array:
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i] - min_element] - 1] = arr[i]
        count_array[arr[i] - min_element] -= 1

    return output_array


if __name__ == '__main__':
    arr = [5, 4, -3, 2, 1]
    print(countingSort(arr))
