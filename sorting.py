import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
        return data


def selection_sort(number_array, direction="ascending"):
    for i in range(len(number_array) - 1):
        min_idx = i
        for num_idx in range(i + 1, len(number_array)):
            if direction == "ascending":
                if number_array[min_idx] > number_array[num_idx]:
                    min_idx = num_idx
            elif  direction == "descending":
                if number_array[min_idx] < number_array[num_idx]:
                    min_idx = num_idx
        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]
    return number_array


def bubble_sort(nums):
    for j in range(len(nums) - 1):
        for num_id in range(len(nums) - 1 - j):
            if nums[num_id] > nums[num_id + 1]:
                nums[num_id], nums[num_id + 1] = nums[num_id + 1], nums[num_id]
    return nums


def insertion_sort(numbers):
    for num_i in range(1, len(numbers)):
        key = numbers[num_i]
        i = num_i - 1
        while i >= 0 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            i = i - 1
        numbers[i + 1] = key
    return numbers


def main():
    data = read_data("numbers.csv")
    print(data)
    sorted = selection_sort(data["series_1"].copy(), "descending")
    print(sorted)
    bubbled = bubble_sort(data["series_1"].copy())
    print(bubbled)
    insertioned = insertion_sort(data["series_1"].copy())
    print(insertioned)


if __name__ == '__main__':
    main()
    my_list = [3, 8, 1, 2, 32]
    my_list.sort()
    my_list = sorted(my_list)
    my_list = sorted(my_list, reverse=True)
    print(my_list)

    list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
    list_of_words = sorted(list_of_words, key=len)
    list_of_words = sorted(list_of_words, key=str.lower)
    print(list_of_words)