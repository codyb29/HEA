import sys
sys.path.append("..")  # input path to installation files here
from core import ea
from rosetta import *
from pyrosetta import *

# arrayJobs = 1  # first argument UNCOMMENT WHEN READY FOR ARGO CLUSTER
protein = 1  # second argument SWITCH BACK TO 2 WHEN READY FOR ARGO CLUSTER
if (len(sys.argv) < 1):  # Check if arguments are provided correctly. CHANGE NUMBER TO APPROPRIATE AMOUNT OF ARGUMENTS FOR THE TIME BEING
    print('Please provide the number of array jobs required and the initialization file.')
    exit(1)

# Upon verification, initialize constants
# ARRAY_ID = sys.argv[arrayJobs] UNCOMMENT WHEN READY FOR ARGO CLUSTER
# FILENAME = sys.argv[protein] UNCOMMENT SOON
# Initialization of the population
score_fxn = create_score_function('score0')
for i in range(0, 200) :
    # TODO: Fragment Replacement




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
