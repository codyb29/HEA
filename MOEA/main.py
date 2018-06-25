import sys
sys.path.append('..')  # input path to installation files here
from core import EA
from rosetta import *
from pyrosetta import *

arrayJobs = 1
protein = 2 
# Check if arguments are provided correctly. CHANGE NUMBER TO APPROPRIATE AMOUNT OF ARGUMENTS FOR THE TIME BEING
if (len(sys.argv) < 3 and len(sys.argv) > 4):
    print('Please provide the number of arraxsy jobs required and the initialization file.')
    exit(1)

# Upon verification, initialize constants
ARRAY_ID = sys.argv[arrayJobs] # pass 0 for the time being to run on local machine
INIT_FILE = sys.argv[protein]

protein = EA (INIT_FILE)
# path/to/file/filename
FILENAME = './../results/' + protein.pdbid + '-' + ARRAY_ID + '-MOEA.txt'
protein.run()

with open (FILENAME, 'a') as fl :
    for score in protein.rmsdarchive :
        fl.write (str(score) + '\n') 




# Initialization of the population
"""
Work on later
score_fxn = create_score_function('score0')
for i in range(0, 200) :
    # TODO: Fragment Replacement
"""


# score4 = create_score_function('score4_smooth') # Currently not needed at the beginning.

# TODO: learn why there's only one iteration and why the for loop is necessary if this is the case.
"""
Does not appear to do what needs to be done.
for i in range(1):
    main = ea(FILENAME)
    main.run()
    with open("/scratch/kzou/"+main.pdbid+'-'+ARRAY_ID+'-MOEA.txt', 'a') as f:
        for score in main.rmsdarchive:
            f.write(str(score)+"\n")
"""

# I believe this portion of the code is written for HEA
# f.write(str(min(main.energyarchive))+"\n")
# for pose in main.population:
#    s = str(core.scoring.CA_rmsd(pose,main.knownNative))+" "+str(score4(pose))+"\n"
#    f.write(s)
