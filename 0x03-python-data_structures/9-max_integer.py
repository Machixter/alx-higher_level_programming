#!/usr/bin/python3
def max_integer(my_list=[]):
    #check if list is empty
    if len(my_list) == 0:
        return (None)
    #assign new var to first element in list
    max_no = my_list[0]
    #iterrate through list
    for x in my_list:
        #compare to find largest int 
        if x > max_no:
            max_no = x
            #return largest int found
    return (max_no)
