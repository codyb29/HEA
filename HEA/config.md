# Project Configuration
## HEA
The baseline of the whole project. This is where the algorithm is implemented to gather information on various protein configurations.

**improvement_modules:** Will evaluate the amino acid chain that make up the protein and attempt to improve the rosetta score entailing a given protein.

**selection_modules:** The selection methodology used to decide how a population of amino acids will be truncated from a pool of parents and children.

**setup_modules:** Accepts .ini files as form of protein information to setup the algorithm with the appropriate information.

**variation_modules:** Varies the protein structure in such a way in order to optimize, with respect to our capabilities, the rosetta score.

**shell_scripts:** Example/Test files that will run the algorithm on the ARGO cluster.

**initialization_files:** The .ini files that are used to feed the setup_modules.

**core.py:** Contains the construction of the pareto_archive data collection methodology along with the construction of an ea object.

**improvement.py:** A slightly more user friendly interface that utilizes the improvement_module to improve the protein score overall.

**main.py:** The De Facto driver of the program. The main entry point of the project.

**selection.py:** Similar to the driving purpose of the improvement.py except implements the selection_module.

**setup.py:** Similar to the driving purpose of the improvement.py except implements the setup_module.

**variation.py:** Similar to the driving purpose of the improvement.py except implements the variation_module.

## proteins
Essential protein files to run the program. These can include pdb files, fasta files, or fragment files.

## results
Title is pretty self explanatory. Contains the evaluated results derived from the program. Also contains a mini-program to plot the data.

## Scatterplot
Simple python script that uses matplotlib to graph the results of the MOEA. Kepts as a quick reference to Kevin's results.