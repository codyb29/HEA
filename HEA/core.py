from rosetta.core.scoring import calpha_superimpose_pose, CA_rmsd
from pyrosetta import Pose
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
            print("Evaluation Status: " + str(int((self.evalnum / self.evalbudget) * 100)) + "%")
            self.iterate()

    def iterate(self):
        # Possible expansion of MOEA. Hence, why this operation is more complicated than it needs to be.
        # Follows the order of [[pose, score], [pose, score], ...]
        prevPop = selection.select(self)
        nextPop = []

        # Focus on the poses
        for i in range(len(prevPop)):
            # Setup variables for creating the new protein configuration to be added to the population.
            tempPose = Pose()
            tempPose.assign(prevPop[i][0]) # copy pose from previous generation.
            posePair = [tempPose, prevPop[i][1]]  # [pose, score]

            # Begin protein manipulation
            crossover.typeofcrossover(self, tempPose)  # Perform a crossover
            variation.perturb(self, posePair)  # Apply fragment replacement
            improvement.localSearch(self, posePair) # Local search for possible improvement
            nextPop.append(posePair)

        for i in range(len(nextPop)):
            # align the poses for a better score.
            calpha_superimpose_pose(nextPop[i][0], self.knownNative)
            # Evaluate and store the rmsd score between the 2 poses.
            self.rmsdarchive.append(CA_rmsd(nextPop[i][0], self.knownNative))

        # Elitest-based Truncation Selection
        self.population = selection.truncate(self, prevPop, nextPop)
