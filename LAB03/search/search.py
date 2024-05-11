# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    frontier = util.Stack()
    # previously explored states (for path checking), holds states
    explored_set = []
    # define start node
    start_state = problem.getStartState()
    start_node = (start_state, [])

    frontier.push(start_node)

    while not frontier.isEmpty():
        # begin exploring last (most-recently-pushed) node on frontier
        current_state, actions = frontier.pop()

        if current_state not in explored_set:
            # mark current node as explored
            explored_set.append(current_state)

            if problem.isGoalState(current_state):
                return actions
            else:
                # get list of possible successor nodes in
                # form (successor, action, stepCost)
                successors = problem.getSuccessors(current_state)

                # push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)

    return actions
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    explored_set = []
    start_state = problem.getStartState()
    start_node = (start_state, [], 0) #(state, action, cost)
    frontier.push(start_node)

    while not frontier.isEmpty():
        # begin exploring first (earliest-pushed) node on frontier
        current_state, actions, current_cost = frontier.pop()

        if current_state not in explored_set:
            # put popped node state into explored list
            explored_set.append(current_state)

            if problem.isGoalState(current_state):
                return actions
            else:
                successors = problem.getSuccessors(current_state)

                for successState, successAction, successCost in successors:
                    new_action = actions + [successAction]
                    new_cost = current_cost + successCost
                    new_node = (successState, new_action, new_cost)

                    frontier.push(new_node)

    return actions
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()

    explored_set = {}

    start_state = problem.getStartState()
    start_node = (start_state, [], 0)  # (state, action, cost)

    frontier.push(start_node, 0)

    while not frontier.isEmpty():
        # begin exploring first (lowest-cost) node on frontier
        current_state, actions, current_cost = frontier.pop()

        if (current_state not in explored_set) or (current_cost < explored_set[current_state]):
            explored_set[current_state] = current_cost

            if problem.isGoalState(current_state):
                return actions
            else:
                successors = problem.getSuccessors(current_state)

                for successState, successAction, successCost in successors:
                    new_action = actions + [successAction]
                    new_cost = current_cost + successCost
                    new_node = (successState, new_action, new_cost)

                    frontier.update(new_node, new_cost)

    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def bestFirstSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # to be explored (FIFO): holds (item, cost)
    frontier = util.PriorityQueue()
    # previously expanded states (for cycle checking), holds state:cost
    exploredNodes = {}
    startState = problem.getStartState()
    startNode = (startState, [], 0)  # (state, action, cost)
    frontier.push(startNode, heuristic(startState, problem))
    while not frontier.isEmpty():
        # begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            # put popped node's state into explored list
            exploredNodes[currentState] = currentCost
            if problem.isGoalState(currentState):
                return actions
            else:
                # list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)
                    frontier.update(newNode, heuristic(succState, problem))
    return actions
    util.raiseNotDefined()


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()

    exploredNodes = []  # holds (state, cost)

    startState = problem.getStartState()
    startNode = (startState, [], 0)  # (state, action, cost)

    frontier.push(startNode, 0)

    while not frontier.isEmpty():
        # begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()
        # put popped node into explored list
        currentNode = (currentState, currentCost)
        exploredNodes.append((currentState, currentCost))
        if problem.isGoalState(currentState):
            return actions
        else:
            # list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)
            # examine each successor
            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (succState, newAction, newCost)
                # check if this successor has been explored
                already_explored = False
                for explored in exploredNodes:
                    # examine each explored node tuple
                    exploredState, exploredCost = explored
                    if (succState == exploredState) and (newCost >= exploredCost):
                        already_explored = True
                # if this successor not explored, put on frontier and explored list
                if not already_explored:
                    frontier.push(newNode, newCost + heuristic(succState, problem))
                    exploredNodes.append((succState, newCost))
    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
