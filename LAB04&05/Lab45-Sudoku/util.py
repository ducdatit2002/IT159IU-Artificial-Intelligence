import inspect
import sys


digits = cols = "123456789"
rows = "ABCDEFGHI"

def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)

def cross(A, B):
    """
    Finding the cross product of two sets
    """
    return [a + b for a in A for b in B]

squares = cross(rows, cols)