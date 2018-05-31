# Abhishek Kundu
# CPE 202
# Assignment 1
# perm_lex.py

def perm_gen_lex(str):
    # Python program to generate all the permutations of the characters in a string
    lst = []
    if len(str) <= 1:  # If the string contains a single character
        lst.append(str)
        return lst  # return a list containing that string
    for i in str:  # for each char in string
        for perm in perm_gen_lex(str.replace(i, '', 1)):  # Generate all permutations of the simpler string recursively
            lst.append(i + perm)  # Add the removed character to the front of each permutation of the simpler word, and add the resulting permutation to a list
    return lst  # Return all these newly constructed permutations in a list
