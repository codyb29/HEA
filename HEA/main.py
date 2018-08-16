import sys
sys.path.append('..')  # input path to installation files here
from pyrosetta import *
from core import EA

arrayJobs = 1
protein = 2 
# Check if arguments are provided correctly. CHANGE NUMBER TO APPROPRIATE AMOUNT OF ARGUMENTS FOR THE TIME BEING
if (len(sys.argv) != 3):
    print('Please provide the number of arraxsy jobs required and the initialization file.')
    exit(1)

# Upon verification, initialize constants
ARRAY_ID = sys.argv[arrayJobs] # pass 0 for the time being to run on local machine
INIT_FILE = sys.argv[protein]

init() # Initialize the pyrosetta library
protein = EA (INIT_FILE) # Initialize Evolutionaryv Algorithm with given protein file
# path/to/file/FILENAME
FILENAME = './../results/' + protein.pdbid + '-' + ARRAY_ID + '-HEA.txt'
protein.run()

with open (FILENAME, 'w') as fl :
    for pd in protein.proteinDB :
        #           RMSD                Score               Age
        fl.write (str(pd[0]) + ' ' + str(pd[1]) + ' ' + str(pd[2]) + '\n')
