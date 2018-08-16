# File breaks down the general template to submit this job on the argo cluster.
#!/bin/sh # Necessary to notify that it will be a shell script
#SBATCH --job-name <job label> # name is pretty self explanatory. Give a name to the job.
#SBATCH -p all-LoPri # Indicate a low Priority job so we don't hog the resources.
#SBATCH -t 0-08:00 # My tests have gone around 8 hours. Different proteins will vary so adjust accordingly. Format: D-hh:mm
#SBATCH --mem 1024 # Again, Different proteins will need more or less memory. Adjust accordingly. Format: # MB
#SBATCH --array=1-5 # Will run it 5 times
#SBATCH -o /scratch/<GMU Username>/slurm.%N.%j.out # output file
#SBATCH -e /scratch/<GMU Username>/slurm.%N.%j.err # error file
#SBATCH --mail-type=FAIL # Will notify upon a failed task
#SBATCH --mail-user=<GMU Email>
source /home/<GMU Username>/<virtual environment name>/bin/activate # Will need to create a virtual environment to get pyrosetta on the argo cluster
python3 main.py $SLURM_ARRAY_TASK_ID initialization_files/<protein of interest> > /dev/null # To run the program and delete unecessary stdout info
deactivate # Deactivate the virtual environment.
