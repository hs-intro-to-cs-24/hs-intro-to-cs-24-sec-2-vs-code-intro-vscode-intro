#!/usr/bin/env python3


def count_nums_between(int_list, min_num, max_num):
    """
    This function counts the number of integers in a list that are between
    `min_num` and `max_num` (inclusive). For example, given t

    :param int_list: The list of numbers
    :param min_num: The minimum number to look for numbers "between"
    :param max_num: The maximum number to look for numbers "between"
    """
    # Replace the code below with your own code
    return -1


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
total_wrong = 0

# Test 1
ret = count_nums_between([1, 2, 3, 4], 0, 5)
if ret != 4:
    print("Test 1: Uh oh, [1, 2, 3, 4] returned", ret)
    total_wrong = total_wrong + 1


# Test 2
ret = count_nums_between([1, 2, -4, -6, 3, 4], 3, 4)
if ret != 2:
    print("Test 2: Uh oh, [1, 2, -4, -6, 3, 4] returned", ret)
    total_wrong = total_wrong + 1


# Test 3
ret = count_nums_between([-5, -1, -2], 10, 12)
if ret != 0:
    print("Test 3: Uh oh, [-5, -1, -2] returned", ret)
    total_wrong = total_wrong + 1


# Test 4
ret = count_nums_between([], 8, 10)
if ret != 0:
    print("Test 4: Uh oh, [] returned", ret)
    total_wrong = total_wrong + 1


# Test 5
ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 0, 2)
if ret != 7:
    print("Test 5: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
    total_wrong = total_wrong + 1


# Test 6
ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 0, 1)
if ret != 7:
    print("Test 6: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
    total_wrong = total_wrong + 1


# Test 7
ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 1, 1)
if ret != 7:
    print("Test 7: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
    total_wrong = total_wrong + 1


# Test 8
ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 1, 2)
if ret != 7:
    print("Test 8: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
    total_wrong = total_wrong + 1


# Test 9
ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 0, 0)
if ret != 0:
    print("Test 9: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
    total_wrong = total_wrong + 1


# Test 10
ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 2, 2)
if ret != 0:
    print("Test 10: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
    total_wrong = total_wrong + 1


if total_wrong == 0:
    print("Overall: Woohoo! All tests have been passed for Problem 7!")
else:
    print("Overall: There's still work to do!")
