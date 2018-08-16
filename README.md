# HEA
An implementation of a Hybrid Evolutionary search Algorithm for GMU's Computational Biology Labratory.

## Get Started Locally
* Install [Pyrosetta](http://www.pyrosetta.org/dow) for Python v3.6 for your respective OS and follow steps on the website.
* See the initialization_files directory to see how to configure your protein of interest for the program.
* Get necessary files (.pdb, .fasta, .200_v1_3) from [RCSB](https://www.rcsb.org/) and [Robetta](http://robetta.bakerlab.org/fragmentsubmit.jsp)
* Configure paths in the code accordingly to your workspace. 
    * main.py asks where your pyrosetta installation is and where you want the results stored.
    * To make things easy, store your protein files in a directory like "proteins/name_of_protein/" and things should work seamlessly.
* If everything was done correctly, simply run: `python3 main.py 0 initialization_files/<protein_name>.ini`
    * The 0 will become important if run on the ARGO cluster. since this is only done locally, simply pass through the 0.
    * the last argument is assuming the workspace is kept the same as here. Otherwise, specify the directory in which the .ini files are located and pass through the protein ini file of interest.

After all that, you should be good to go!

## Project Configuration

### HEA
The baseline of the whole project. This is where the algorithm is implemented to gather information on various protein configurations.

**improvement_modules:** Will evaluate the amino acid chain that make up the protein and attempt to improve the rosetta score entailing a given protein.

**crossover_modules:** Library of functions that can implement a crossover between two proteins within the program. A module was created for potential expansion on this.

**selection_modules:** The selection methodology used to decide how a population of amino acids will be truncated from a pool of parents and children.

**setup_modules:** Accepts .ini files as form of protein information to setup the algorithm with the appropriate information.

**variation_modules:** Varies the protein structure in such a way in order to optimize, with respect to our capabilities, the rosetta score.

**initialization_files:** Example and Template .ini file that are required to specify the type of protein to be initialized for the program. There is also a template shell script for running it on the ARAGO cluster.

**core.py:** Contains the construction of the pareto_archive data collection methodology along with the construction of an ea object.

**improvement.py:** A slightly more user friendly interface that utilizes the improvement_module to improve the protein score overall.

**main.py:** The De Facto driver of the program. The main entry point of the project.

**selection.py:** Similar to the driving purpose of the improvement.py except implements the selection_module.

**setup.py:** Similar to the driving purpose of the improvement.py except implements the setup_module.

**variation.py:** Similar to the driving purpose of the improvement.py except implements the variation_module.

### proteins
Essential protein files to run the program. These can include pdb files, fasta files, or fragment files (.200_v1_3). There's already a few in here to get things started quickly.

### results
Title is pretty self explanatory. By default, where the results will be stored after the program is finished. Also contains a graphing tool to visualize your results.


