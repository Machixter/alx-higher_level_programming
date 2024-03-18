#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #if tuple_a is < 2, use 0
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    #if tuble_b is < 2, use 0
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
        
    #add the first element of each tuple 
    first_element = tuple_a[0] + tuple_b[0]
    #add the second element of each tuple
    second_element = tuple_a[1] + tuple_b[1]

    #return a tuple with the addition of the first and second elements
    return (first_element, second_element)
