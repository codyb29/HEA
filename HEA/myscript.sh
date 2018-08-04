#!/bin/sh
#SBATCH --job-name hea1ail
#SBATCH --partition all-LoPri
#SBATCH --time 0-00:10:00
#SBATCH --array=1-5
#SBATCH -o /scratch/cbarre15/.outerr-%j # output file
#SBATCH -e /scratch/cbarre15/.output-%j # error file
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=cbarre15@gmu.edu
source /home/cbarre15/rosettaEnv/bin/activate
python3 main.py $SLURM_ARRAY_TASK_ID initialization_files/1ail.ini > /dev/null
deactivate
