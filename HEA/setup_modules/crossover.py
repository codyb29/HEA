from pyrosetta import *
from rosetta import *

def crossover(eaObj, cocfg):
    eaObj.cotype = int(cocfg['cotype']) 
    # The type of crossover we want to do (1 = 1-point, 2 = 2-point, 3 = homologous 1-point)