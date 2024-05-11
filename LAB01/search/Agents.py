from game import Agent
from game import Directions
from util import manhattanDistance
import random
import util
class DumbAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions:
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping")
            return Directions.STOP

class RandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        return random.choice(state.getLegalPacmanActions())


class BetterRandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        rSA = state.getLegalPacmanActions()
        rSA.remove(rSA[-1])
        print("Action available: ", rSA)
        return random.choice(rSA)


class ReflexAgent(Agent):

    def getAction(self, gameState):

        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):

        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        food_left = sum(int(j) for i in newFood for j in i)

        if food_left > 0:
            food_distances = [manhattanDistance(newPos, (x, y))
                              for x, row in enumerate(newFood)
                              for y, food in enumerate(row)
                              if food]
            shortest_food = min(food_distances)
        else:
            shortest_food = 0


def scoreEvaluationFunction(currentGameState):
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)