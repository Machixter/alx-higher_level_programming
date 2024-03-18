#!/usr/bin/python3

def multiple_returns(sentence):
    #check if sentence is empty
    if sentence == "":
        return (None, None)
    else:
        return (len(sentence), sentence[0])
