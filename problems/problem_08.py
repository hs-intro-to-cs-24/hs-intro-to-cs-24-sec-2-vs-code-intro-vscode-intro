#!/usr/bin/env python3


def look_smart(sentence):
    """
    This function replaces all the words in a sentence that are short (less than
    four letters) with "paradigm shifting" just to look smart.

    :param sentence: The phrase to make smarter
    """
    # Replace the code below with your own code
    return "paradigm shifting"


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
total_wrong = 0

# Test 1
ret = look_smart("This seems fun")
if ret != "This seems paradigm shifting":
    print('Test 1: Uh oh, "This seems fun" returned', ret)
    total_wrong = total_wrong + 1


# Test 2
ret = look_smart("Hi there Dan")
if ret != "paradigm shifting there paradigm shifting":
    print('Test 2: Uh oh, "Hi there Dan" returned', ret)
    total_wrong = total_wrong + 1


# Test 3
ret = look_smart("This sentence refuses words below length four")
if ret != "This sentence refuses words below length four":
    print('Test 3: Uh oh, "This sentence refuses words below length four" returned', ret)
    total_wrong = total_wrong + 1


# Test 4
ret = look_smart("yo")
if ret != "paradigm shifting":
    print('Test 4: Uh oh, "yo" returned', ret)
    total_wrong = total_wrong + 1


# Test 5
ret = look_smart("encyclopedia")
if ret != "encyclopedia":
    print('Test 5: Uh oh, "encyclopedia" returned', ret)
    total_wrong = total_wrong + 1


if total_wrong == 0:
    print("Overall: Woohoo! All tests have been passed for Problem 8!")
else:
    print("Overall: There's still work to do!")
