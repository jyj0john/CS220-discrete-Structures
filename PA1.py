# CS220 - Programming Assignment 1 : Boolean Logic
# author - Asa Ben-Hur and Nirmal Prajapati

# NOTE:
# You must use small single letters for your variable names, for eg. a, b, c
# You may use parenthesis to group your expressions such as 'a and (b or c)'

# Implement the following four functions:
# truth_table, count_satisfying, is_tautology and are_equivalent

# Submission:
# Submit this file using the checkin system on the course web page.



######## Do not modify the following block of code ########
# ********************** BEGIN *******************************

from functools import partial
import re


class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q) :
    return not p or q

@Infix
def iff(p, q) :
    return (p |implies| q) and (q |implies| p)


# You must use this function to extract variables
# This function takes an expression as input and returns a sorted list of variables
# Do NOT modify this function
def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

# *********************** END ***************************




############## IMPLEMENT THE FOLLOWING FUNCTIONS  ##############
############## Do not modify function definitions ##############


# This function calculates a truth table for a given expression
# input: expression
# output: truth table as a list of lists
# You must use extract_variables function to generate the list of variables from expression
# return a list of lists for this function
def truth_va(a_list,num):
    n = len(a_list)
    if num == 0:
        a_list.insert(0,False)
        
        return a_list
    elif num == 1:
        a_list.insert(0,True)
       
        return a_list
    else:
        if num%2 == 0:
            a_list.insert(0,False)
            
            return truth_va(a_list, num/2)
        else:
            a_list.insert(0,True)
            
            return truth_va(a_list,(int)(num/2))
def truth_table(expression):
    variable = extract_variables(expression)
    n = len(variable)
    
    values = []
    for i in range(2**n):
        result = []
        result = truth_va(result,i)
        while len(result) < n:
            result.insert(0,False)
        for j in range(n):
            exec(variable[j] + '=' + str(result[j]))
        case = result.copy()
        case.append(eval(expression))
        values.append(case[:])
            
    return values
# count the number of satisfying values
# input: expression
# output: number of satisfying values in the expression
def count_satisfying(expression):
    a_list = truth_table(expression)
    count = 0
    for i in range(len(a_list)):            
        if a_list[i][len(a_list[i])-1] == True:
            count += 1
    return count

# if the expression is a tautology return True,
# False otherwise
# input: expression
# output: bool
def is_tautology(expression):
    a_list = truth_table(expression)
    count = count_satisfying(expression)
    if count == len(a_list):
        return True
    else:
        return False
# if expr1 is equivalent to expr2 return True,
# False otherwise
# input: expression 1 and expression 2
# output: bool
def are_equivalent(expr1, expr2):
    
    a_list = truth_table(expr1)
    b_list = truth_table(expr2)
    if extract_variables(expr1) == extract_variables(expr2):
        if a_list == b_list:
            return True
        else:
            return False
    else:
        return False

