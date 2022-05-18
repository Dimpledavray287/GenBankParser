# Parse-GenBank-file-to-retrieved-adjacent-genes-of-specific-genes
Parse GenBank file to retrieved adjacent genes of specific genes.
Description: This pipeline contains 2 programs which are run in sequence: Parse1.py and Parse2.py. The output of Parse1.py is used by Parse2.py program.

Parse1.py: 
A single GenBank file is a text file as input file which contains information about multiple Genomes. 
This program parses only those Genomes which contains the Product Name of the Gene which is passed as a parameter in the findProduct variables.
It program generates a .CSV file which contains the following attributes of the Gene:  Version, CDS, Product, ProteinId, LocusTag. 

Parse2.py: 
This program retrieves adjacent genes located above and below the specific genes (findProduct variable) in the .CSV file which was generated as an output from Parse1 program. The findproduct variable should be same in Parse1 and Parse2 program. 
The number of genes to be retrieved above and below can be decide as per the user choice.
