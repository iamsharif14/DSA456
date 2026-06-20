import random
import time


def bubble_sort(my_list):
    steps = 0
    n = len(my_list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps = steps + 1

            if my_list[j] > my_list[j + 1]:
                steps = steps + 4
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return steps


def selection_sort(my_list):
    steps = 0
    n = len(my_list)

    for i in range(n - 1):
        min_idx = i
        steps = steps + 1

        for j in range(i + 1, n):
            steps = steps + 1

            if my_list[j] < my_list[min_idx]:
                min_idx = j
                steps = steps + 1

        if min_idx != i:
            steps = steps + 4
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

    return steps


def insertion_sort(my_list):
    steps = 0

    for i in range(1, len(my_list)):
        curr = my_list[i]
        j = i
        steps = steps + 2

        while j > 0 and my_list[j - 1] > curr:
            steps = steps + 1
            my_list[j] = my_list[j - 1]
            j = j - 1
            steps = steps + 2

        my_list[j] = curr
        steps = steps + 1

    return steps


def insertion_sort_part(my_list, left, right): #Different name, since python can not have two functions with the same name.
    steps = 0

    for i in range(left + 1, right + 1):
        curr = my_list[i]
        j = i
        steps = steps + 2

        while j > left and my_list[j - 1] > curr:
            steps = steps + 1
            my_list[j] = my_list[j - 1]
            j = j - 1
            steps = steps + 2

        my_list[j] = curr
        steps = steps + 1

    return steps


def partition(my_list, left, right):
    steps = 0

    pivot_location = random.randint(left, right)
    pivot = my_list[pivot_location]
    steps = steps + 2

    my_list[pivot_location] = my_list[right]
    my_list[right] = pivot
    steps = steps + 2

    end_of_smaller = left - 1
    steps = steps + 1

    for j in range(left, right):
        steps = steps + 1

        if my_list[j] <= pivot:
            end_of_smaller = end_of_smaller + 1
            my_list[end_of_smaller], my_list[j] = my_list[j], my_list[end_of_smaller]
            steps = steps + 4

    my_list[end_of_smaller + 1], my_list[right] = my_list[right], my_list[end_of_smaller + 1]
    steps = steps + 4

    return end_of_smaller + 1, steps


def recursive_quick_sort(my_list, left, right):
    steps = 0

    if right - left <= 32:
        steps = steps + insertion_sort_part(my_list, left, right)
    else:
        pivot_position, partition_steps = partition(my_list, left, right)
        steps = steps + partition_steps

        steps = steps + recursive_quick_sort(my_list, left, pivot_position - 1)
        steps = steps + recursive_quick_sort(my_list, pivot_position + 1, right)

    return steps


def quick_sort(my_list):
    steps = recursive_quick_sort(my_list, 0, len(my_list) - 1)
    return steps



# main function
def main():
    sizes = [10, 50, 100, 500, 1000, 5000]

    for size in sizes:

        rand_list = [random.randint(0, 101) for i in range(size)]
        rand_list.sort(reverse=True)

        print("\nList Size:", size)

        list1 = rand_list.copy()
        start = time.time()
        bubble_steps = bubble_sort(list1)
        bubble_time = time.time() - start
        print("Bubble Sort steps needed: {}".format(bubble_steps))
        print("Bubble Sort time: {:.6f} \n".format(bubble_time))

        list2 = rand_list.copy()
        start = time.time()
        selection_steps = selection_sort(list2)
        selection_time = time.time() - start
        print("Selection Sort steps needed: {}".format(selection_steps))
        print("Selection Sort time: {:.6f} \n".format(selection_time))

        list3 = rand_list.copy()
        start = time.time()
        insertion_steps = insertion_sort(list3)
        insertion_time = time.time() - start
        print("Insertion Sort steps needed: {}".format(insertion_steps))
        print("Insertion Sort time: {:.6f} \n".format(insertion_time))

        list4 = rand_list.copy()
        start = time.time()
        quick_steps = quick_sort(list4)
        quick_time = time.time() - start
        print("Quick Sort steps needed: {}".format(quick_steps))
        print("Quick Sort time: {:.6f} \n".format(quick_time))


main()