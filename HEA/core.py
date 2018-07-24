from pyrosetta import *
from rosetta import core
import setup
import variation
import improvement
import selection
import crossover


class EA:
    def __init__(self, cfg):
        setup.run(self, cfg)  # Initializes necessary variables.
        self.rmsdarchive = []  # Archive of all the scores evaluated

    def run(self):
        self.evalnum = 0
        while (self.evalnum < self.evalbudget):
            print(self.evalnum)
            self.iterate()
        self.evalnum = 0 # TODO: Potentially delete. No idea why the reset is needed if program finishes.

    def iterate(self):
        # Possible expansion of MOEA. Hence, why this operation is more complicated than it needs to be.
        # Follows the order of [pose, score, pose, score, ...]
        prevPop = selection.select(self)
        nextPop = []

        # Focus on the poses
        for i in range(len(prevPop)):
            # Setup variables for creating the new protein configuration to be added to the population.
            tempPose = Pose()
            # copy pose from previous generation.
            tempPose.assign(prevPop[i][0])
            # Easy insertion of our designated format.
            posePair = [tempPose, prevPop[i][1]]

            tempPose = crossover.typeofcrossover(
                self, tempPose)  # Perform a crossover
            variation.perturb(self, posePair)  # Apply fragment replacement
            # Local search for possible improvement
            improvement.localSearch(self, posePair)
            # Add manipulated child protein to the new population
            nextPop.append(posePair)

        # Get RMSD scores from our newly created population. Essentially, our evaluation phase.
        for i in range(len(nextPop)):
            self.rmsdarchive.append(
                core.scoring.CA_rmsd(nextPop[i][0], self.knownNative))

        # Elitest-based Truncation Selection
        self.population = selection.truncate(self, prevPop, nextPop)
