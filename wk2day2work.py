
# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def less_then_ten(alist):
    new_alist = []
    for number in alist:
        if number <= 9:
            new_alist.append(number)
        else:
            continue
    return new_alist            


# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merged_sort(list1,list2):
    merged_lists = list1 + list2
    merged_lists.sort()
    return merged_lists

