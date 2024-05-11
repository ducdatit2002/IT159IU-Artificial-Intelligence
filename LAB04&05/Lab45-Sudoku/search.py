"""
In search.py, you will implement Backtracking and AC3 searching algorithms
for solving Sudoku problem which is called by sudoku.py
"""

from csp import *
from copy import deepcopy
import util



def Backtracking_Search(csp):
    return Recursive_Backtracking({}, csp)


def Recursive_Backtracking(assignment, csp):
    if isComplete(assignment):
        return assignment

    var = Select_Unassigned_Variables(assignment, csp)
    domain = deepcopy(csp.values)

    for value in csp.values[var]:
        if isConsistent(var, value, assignment, csp):
            assignment[var] = value
            inferences = {}
            inferences = Inference(assignment, inferences, csp, var, value)
            if inferences!= "FAILURE":
                result = Recursive_Backtracking(assignment, csp)
                if result!="FAILURE":
                    return result

            del assignment[var]
            csp.values.update(domain)
    return "FAILURE"

def Inference(assignment, inferences, csp, var, value):
    """
    Forward checking using concept of Inferences
    """

    inferences[var] = value

    for neighbor in csp.peers[var]:
        if neighbor not in assignment and value in csp.values[neighbor]:
            if len(csp.values[neighbor]) == 1:
                return "FAILURE"

            remaining = csp.values[neighbor] = csp.values[neighbor].replace(value, "")

            if len(remaining) == 1:
                flag = Inference(assignment, inferences, csp, neighbor, remaining)
                if flag == "FAILURE":
                    return "FAILURE"

    return inferences

def Order_Domain_Values(var, assignment, csp):
    """
    Returns string of values of given variable
    """
    return csp.values[var]

def Select_Unassigned_Variables(assignment, csp):
    """
    Selects new variable to be assigned using minimum remaining value (MRV)
    """
    unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv

def isComplete(assignment):
    """
    Check if assignment is complete
    """
    return set(assignment.keys()) == set(squares)

def isConsistent(var, value, assignment, csp):
    """
    Check if assignment is consistent
    """
    for neighbor in csp.peers[var]:
        if neighbor in assignment.keys() and assignment[neighbor] == value:
            return False
    return True

def forward_checking(csp, assignment, var, value):
    csp.values[var] = value
    for neighbor in csp.peers[var]:
        csp.values[neighbor] = csp.values[neighbor].replace(value, '')

def display(values):
    """
    Display the solved sudoku on screen
    """
    for row in rows:
        if row in 'DG':
            print("-------------------------------------------")
        for col in cols:
            if col in '47':
                print(' | ', values[row + col], ' ', end=' ')
            else:
                print(values[row + col], ' ', end=' ')
        print(end='\n')

def write(values):
    """
    Write the string output of solved sudoku to file
    """
    output = ""
    for variable in squares:
        output = output + values[variable]
    return output