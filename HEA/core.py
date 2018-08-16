from rosetta.core.scoring import calpha_superimpose_pose, CA_rmsd
from setup_modules.population import ProteinData
from pyrosetta import Pose
from math import inf
import setup
import variation
import improvement
import selection
import crossover


class EA:
    def __init__(self, cfg):
        setup.run(self, cfg)  # Initializes necessary variables.
        self.proteinDB = []  # Archive of all the scores evaluated

    def run(self):
        self.evalnum = 0
        while (self.evalnum < self.evalbudget):
            print("Evaluation Status: " +
                  str(int((self.evalnum / self.evalbudget) * 100)) + "%")
            self.iterate()

    def iterate(self):
        # Possible expansion of MOEA. Hence, why this operation is more complicated than it needs to be.
        prevPop = selection.select(self)
        nextPop = []

        # Focus on the poses
        for i in range(len(prevPop)):
            # Setup variables for creating the new protein configuration to be added to the population.
            childData = ProteinData(Pose(), prevPop[i].score)
            # copy pose from previous generation.
            childData.pose.assign(prevPop[i].pose)

            # Begin protein manipulation
            crossover.typeofcrossover(self, childData)  # Perform a crossover
            variation.perturb(self, childData)  # Apply fragment replacement
            # Local search for possible improvement
            improvement.localSearch(self, childData)
            nextPop.append(childData)

        # Elitest-based Truncation Selection
        self.population = selection.truncate(self, prevPop, nextPop)

        # Evaluate the newest generation
        for i in range(len(self.population)):
            # align the poses for a better score.
            # Don't think this is working. Tested it and didn't show any signficant changes.
            # calpha_superimpose_pose(self.population[i].pose, self.knownNative)
            # Evaluate and store the rmsd score between the 2 poses along with the score.
            self.population[i].rmsd = CA_rmsd(self.population[i].pose, self.knownNative)
            self.population[i].age += 1
            self.proteinDB.append(
                [
                    self.population[i].rmsd, 
                    self.population[i].score, 
                    self.population[i].age
                ]
            )
