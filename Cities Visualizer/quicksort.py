# name: Stephen Wang
# date: November 7, 2020
# purpose: Quicksort algorithm

def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p - 1
    j = p

    for k in range(p, r):
        if compare_func(the_list[k], pivot):
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
        j += 1

    the_list[r], the_list[i+1] = the_list[i+1], the_list[r]
  
    return i + 1

def quicksort(the_list, p, r, compare_func):
    if r > p:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)

def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)
    return the_list

def compare_items(a, b):
    if a <= b:
        return True
    else:
        return False